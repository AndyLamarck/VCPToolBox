#!/usr/bin/env node

// 表情包库设置工具 - 为VCPChat配置表情包
// 作者: 浮浮酱 (◡‿◡✿)

const fs = require('fs').promises;
const path = require('path');

// --- 配置路径 ---
const VCP_TOOLBOX_IMAGE_DIR = path.join(__dirname, 'image');
const VCP_CHAT_APPDATA_DIR = path.join(__dirname, '..', 'VCPChat-main', 'AppData');
const VCP_CHAT_GENERATED_LISTS_DIR = path.join(VCP_CHAT_APPDATA_DIR, 'generated_lists');

// --- 工具函数 ---
function debugLog(message, ...args) {
    console.log(`[表情包设置工具] ${message}`, ...args);
}

async function ensureDirectoryExists(dirPath) {
    try {
        await fs.access(dirPath);
    } catch {
        await fs.mkdir(dirPath, { recursive: true });
        debugLog(`创建目录: ${dirPath}`);
    }
}

async function findEmoticonDirectories(baseDir) {
    try {
        const entries = await fs.readdir(baseDir, { withFileTypes: true });
        return entries
            .filter(entry => entry.isDirectory())
            .filter(entry => entry.name.includes('表情包') || ['angry', 'baka', 'color', 'confused', 'cpu', 'fluxgen', 'fool', 'givemoney', 'happy', 'like', 'meow', 'morning', 'reply', 'sad', 'see', 'shy', 'sigh', 'sleep', 'surprised', 'work'].includes(entry.name))
            .map(entry => entry.name);
    } catch (error) {
        console.error(`[错误] 无法读取目录 ${baseDir}:`, error.message);
        return [];
    }
}

async function generateEmoticonList(emoticonDir, baseDir, outputDir) {
    const emoticonPath = path.join(baseDir, emoticonDir);
    const outputFileName = `${emoticonDir}.txt`;
    const outputFilePath = path.join(outputDir, outputFileName);

    try {
        const files = await fs.readdir(emoticonPath);
        const imageFiles = files.filter(file =>
            /\.(jpg|jpeg|png|gif|webp|bmp)$/i.test(file)
        );

        if (imageFiles.length === 0) {
            debugLog(`⚠️  表情包目录 ${emoticonDir} 中没有找到图片文件`);
            return false;
        }

        const listContent = imageFiles.join('|');
        await fs.writeFile(outputFilePath, listContent);
        debugLog(`✅ 生成表情包列表: ${outputFileName} (${imageFiles.length} 个表情)`);
        return true;

    } catch (error) {
        console.error(`[错误] 处理表情包 ${emoticonDir} 时出错:`, error.message);
        return false;
    }
}

async function readSettings() {
    const settingsPath = path.join(__dirname, '..', 'VCPChat-main', 'AppData', 'settings.json');
    try {
        const content = await fs.readFile(settingsPath, 'utf-8');
        return JSON.parse(content);
    } catch (error) {
        debugLog(`⚠️  无法读取settings.json，将创建默认配置`);
        return {};
    }
}

async function createConfigEnv() {
    const configEnvPath = path.join(VCP_CHAT_GENERATED_LISTS_DIR, 'config.env');

    try {
        await fs.access(configEnvPath);
        debugLog(`✅ config.env已存在`);
        return true;
    } catch {
        // 创建默认config.env
        const defaultConfig = `# 表情包访问配置
# 请根据您的VCP服务器配置修改以下内容
file_key=your_password_here
`;
        await fs.writeFile(configEnvPath, defaultConfig);
        debugLog(`✅ 创建默认config.env文件`);
        console.log(`\n📝 重要提示: 请编辑 ${configEnvPath} 文件，设置正确的 file_key`);
        return false;
    }
}

async function main() {
    console.log('🎭 VCPChat 表情包库设置工具');
    console.log('========================\n');

    // 检查图片目录
    try {
        await fs.access(VCP_TOOLBOX_IMAGE_DIR);
    } catch {
        console.error(`❌ 错误: 图片目录不存在: ${VCP_TOOLBOX_IMAGE_DIR}`);
        console.log('请确保VCPToolBox的image目录存在且包含表情包文件夹');
        process.exit(1);
    }

    // 创建必要的目录
    await ensureDirectoryExists(VCP_CHAT_GENERATED_LISTS_DIR);

    // 查找所有表情包目录
    debugLog('🔍 扫描表情包目录...');
    const emoticonDirs = await findEmoticonDirectories(VCP_TOOLBOX_IMAGE_DIR);

    if (emoticonDirs.length === 0) {
        console.log('❌ 没有找到表情包目录');
        debugLog('请确保表情包目录名称包含"表情包"或是预定义的英文分类名');
        process.exit(1);
    }

    console.log(`📁 找到 ${emoticonDirs.length} 个表情包目录:`);
    emoticonDirs.forEach(dir => console.log(`   - ${dir}`));

    // 生成表情包列表
    console.log('\n📝 生成表情包列表...');
    let successCount = 0;

    for (const emoticonDir of emoticonDirs) {
        const success = await generateEmoticonList(emoticonDir, VCP_TOOLBOX_IMAGE_DIR, VCP_CHAT_GENERATED_LISTS_DIR);
        if (success) successCount++;
    }

    console.log(`\n✅ 成功生成 ${successCount}/${emoticonDirs.length} 个表情包列表`);

    // 处理配置文件
    console.log('\n⚙️  处理配置文件...');

    const settings = await readSettings();
    const configExists = await createConfigEnv();

    if (!settings.vcpServerUrl) {
        console.log('\n📝 VCP服务器URL配置:');
        console.log('请确保VCPChat的settings.json中包含正确的vcpServerUrl');
        console.log('例如: "http://localhost:8080" 或您的VCP服务器地址');
    } else {
        console.log(`✅ VCP服务器URL: ${settings.vcpServerUrl}`);
    }

    // 输出总结
    console.log('\n🎉 设置完成！');
    console.log('========================');
    console.log('📋 已完成以下操作:');
    console.log(`   ✅ 扫描表情包目录: ${VCP_TOOLBOX_IMAGE_DIR}`);
    console.log(`   ✅ 生成表情包列表: ${VCP_CHAT_GENERATED_LISTS_DIR}`);
    console.log(`   ✅ 创建配置文件: ${configExists ? '已存在' : '新建'}`);

    if (!configExists) {
        console.log('\n⚠️  下一步操作:');
        console.log('1. 编辑 config.env 文件，设置正确的 file_key');
        console.log('2. 确保 settings.json 中有正确的 vcpServerUrl');
        console.log('3. 重启 VCPChat 应用');
    } else {
        console.log('\n🚀 使用说明:');
        console.log('1. 重启 VCPChat 应用');
        console.log('2. URL修复器将自动加载表情包库');
        console.log('3. 修复器会自动修复失效的表情包链接');
    }

    console.log('\n💡 提示: 如果添加了新的表情包，请重新运行此工具');
}

// 运行主程序
main().catch(console.error);