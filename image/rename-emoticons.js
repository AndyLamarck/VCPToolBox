#!/usr/bin/env node

// 表情包智能打标重命名工具
// 作者: 浮浮酱 (◡‿◡✿)
// 功能: 读取图片，AI分析内容，生成语义化文件名

const fs = require('fs').promises;
const path = require('path');

// === 配置 ===
const IMAGE_BASE_DIR = __dirname;
const RENAME_MAP_FILE = path.join(__dirname, 'rename-map.json');

// 需要处理的分类 (英文分类有无意义的文件名)
const CATEGORIES_TO_PROCESS = [
    'angry', 'baka', 'color', 'confused', 'cpu', 'fluxgen',
    'fool', 'givemoney', 'happy', 'like', 'meow', 'morning',
    'reply', 'sad', 'see', 'shy', 'sigh', 'sleep', 'surprised', 'work'
];

// 分类的语义提示 (帮助AI理解上下文)
const CATEGORY_HINTS = {
    'angry': '生气、愤怒、不满的表情',
    'baka': '傻瓜、笨蛋、调侃的表情',
    'color': '彩色、多彩的表情',
    'confused': '困惑、疑惑、不解的表情',
    'cpu': 'CPU、计算机相关的表情',
    'fluxgen': 'Flux生成的图片',
    'fool': '愚蠢、搞笑的表情',
    'givemoney': '给钱、打赏、红包相关',
    'happy': '开心、快乐、高兴的表情',
    'like': '喜欢、点赞、支持的表情',
    'meow': '猫咪、喵喵叫的表情',
    'morning': '早晨、起床相关的表情',
    'reply': '回复、响应的表情',
    'sad': '伤心、难过、悲伤的表情',
    'see': '看、观察、注视的表情',
    'shy': '害羞、腼腆、脸红的表情',
    'sigh': '叹气、无奈、疲惫的表情',
    'sleep': '睡觉、困倦的表情',
    'surprised': '惊讶、震惊、意外的表情',
    'work': '工作、劳动相关的表情'
};

// 辅助函数
function debugLog(message, ...args) {
    console.log(`[表情包打标工具] ${message}`, ...args);
}

// 扫描指定分类的所有图片
async function scanCategory(category) {
    const categoryPath = path.join(IMAGE_BASE_DIR, category);

    try {
        const files = await fs.readdir(categoryPath);
        const imageFiles = files.filter(file =>
            /\.(jpg|jpeg|png|gif|webp|bmp)$/i.test(file)
        );

        return imageFiles.map(file => ({
            category: category,
            originalName: file,
            fullPath: path.join(categoryPath, file),
            extension: path.extname(file)
        }));
    } catch (error) {
        console.error(`[错误] 无法读取目录 ${categoryPath}:`, error.message);
        return [];
    }
}

// 第一阶段: 扫描所有需要重命名的图片
async function scanAllImages() {
    debugLog('🔍 开始扫描表情包图片...');

    const allImages = [];

    for (const category of CATEGORIES_TO_PROCESS) {
        const images = await scanCategory(category);
        allImages.push(...images);
        debugLog(`   ✅ ${category}: ${images.length} 张图片`);
    }

    debugLog(`📊 扫描完成，共找到 ${allImages.length} 张需要重命名的图片`);
    return allImages;
}

// 保存扫描结果
async function saveScanResults(images) {
    const scanResultPath = path.join(__dirname, 'scan-results.json');
    await fs.writeFile(scanResultPath, JSON.stringify(images, null, 2));
    debugLog(`💾 扫描结果已保存到: ${scanResultPath}`);
}

// 主函数
async function main() {
    console.log('🎭 表情包智能打标重命名工具');
    console.log('作者: 浮浮酱 (◡‿◡✿)');
    console.log('================================\n');

    // 第一步: 扫描所有图片
    const images = await scanAllImages();

    if (images.length === 0) {
        console.log('❌ 没有找到需要处理的图片');
        process.exit(1);
    }

    // 保存扫描结果供后续使用
    await saveScanResults(images);

    console.log('\n📋 下一步操作:');
    console.log('1. 浮浮酱会分批读取图片进行AI分析');
    console.log('2. 为每张图片生成语义化的文件名');
    console.log('3. 生成重命名映射文件 (rename-map.json)');
    console.log('4. 执行批量重命名操作');
    console.log('\n⚠️  注意: 这是一个分步骤的过程，请跟随浮浮酱的指引操作 (◡‿◡✿)');
}

// 运行主程序
main().catch(console.error);
