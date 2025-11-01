# 表情包重命名指南 (◡‿◡✿)

> 作者: 浮浮酱
> 目标: 将无意义的文件名改为语义化的英文名称

---

## 📋 重命名原则

### 1. 命名格式
```
{分类}-{情绪/动作}-{编号}.{扩展名}

示例:
- angry-yelling-01.jpg      (生气-大喊-编号01)
- happy-smile-01.png         (开心-微笑-编号01)
- sad-crying-01.gif          (伤心-哭泣-编号01)
```

### 2. 命名规范
- ✅ 全部使用**小写字母**
- ✅ 单词之间用**连字符** `-` 连接
- ✅ 编号使用**两位数字** (01, 02, 03...)
- ✅ **保持原始扩展名** (.jpg, .png, .gif等)
- ❌ 不要使用空格、下划线、中文

### 3. 情绪/动作词汇参考

#### angry (生气) - 76张
```
yelling, shouting, furious, rage, mad, annoyed, upset,
frustrated, grumpy, angry-face, red-face, steam, devil,
fist, pointing, scowling, pouting
```

#### happy (开心) - 31张
```
smile, laugh, grin, joy, cheerful, excited, pleased,
dancing, clapping, thumbs-up, heart-eyes, star-eyes,
sparkle, beam, giggle, celebrate
```

#### sad (伤心) - 27张
```
crying, tears, sobbing, depressed, gloomy, disappointed,
heartbroken, teardrop, blue, down, lonely, weeping
```

#### confused (困惑) - 30张
```
puzzled, thinking, wondering, question-mark, scratching-head,
uncertain, perplexed, head-tilt, hmm, what
```

#### shy (害羞) - 43张
```
blushing, embarrassed, shy-smile, hiding, peek, covering-face,
red-cheeks, timid, bashful, nervous
```

#### surprised (惊讶) - 28张
```
shocked, amazed, wow, gasp, open-mouth, wide-eyes,
astonished, startled, surprise-face
```

#### sleep (睡觉) - 8张
```
sleeping, snoring, zzz, tired, yawn, pillow, drowsy, nap
```

#### like (喜欢) - 15张
```
thumbs-up, heart, love, approve, good, ok, nice,
nod, agree, support
```

#### see (看) - 27张
```
looking, staring, watching, observing, peek, glance,
eyes, gaze, notice, spy
```

#### sigh (叹气) - 14张
```
sighing, exhale, weary, tired-sigh, fed-up, exhausted,
giving-up, hopeless
```

#### work (工作) - 1张
```
working, typing, office, computer, busy
```

#### 其他分类
- **baka**: stupid, idiot, dumb, silly, fool-face
- **color**: colorful, rainbow, bright, multi-color
- **cpu**: computer, robot, tech, digital, chip
- **fluxgen**: generated, ai-art, synthetic
- **fool**: silly, goofy, derp, dumb-face, clown
- **givemoney**: money, coin, pay, cash, dollar, tip
- **meow**: cat, kitty, kitten, meow-face, paw
- **morning**: sunrise, morning, wake-up, good-morning
- **reply**: reply, response, answer, talking

---

## 🛠️ 重命名方法

### 方法 A: Windows 文件资源管理器 (推荐新手)

1. 打开目录: `D:\vcp\VCPToolBox-main\image\angry`
2. 切换到**大图标**或**缩略图**视图
3. 逐个查看图片内容
4. 右键点击文件 → **重命名** (或按 `F2`)
5. 输入新文件名 (例如: `angry-yelling-01.jpg`)
6. 按 `Enter` 确认

**优点**: 直观、安全、可以预览图片
**缺点**: 手动逐个操作，速度较慢

---

### 方法 B: 批量重命名工具 (推荐高效)

#### 推荐工具: [Bulk Rename Utility](https://www.bulkrenameutility.co.uk/)

1. 下载并安装 Bulk Rename Utility (免费)
2. 打开软件，导航到 `D:\vcp\VCPToolBox-main\image\angry`
3. 选择所有图片文件
4. 在右侧面板配置:
   - **Name (2)**: 选择 `Replace`
   - **Replace**: 输入当前文件名模式 (如 `1739433`)
   - **With**: 输入新的前缀 (如 `angry-`)
5. 查看预览效果
6. 点击 **Rename** 执行

**优点**: 批量处理、支持正则表达式、可预览
**缺点**: 需要学习工具使用

---

### 方法 C: PowerShell 脚本 (推荐程序员)

浮浮酱已经为主人准备了一个 PowerShell 脚本模板：

```powershell
# 进入目录
cd "D:\vcp\VCPToolBox-main\image\angry"

# 手动创建重命名映射
$renameMap = @{
    "0FFD1AFA5CD0866B1065AEAF45D4066A.jpg" = "angry-yelling-01.jpg"
    "1739433376_1.png" = "angry-furious-02.png"
    "1739433584_1.jpg" = "angry-mad-03.jpg"
    # ... 继续添加映射
}

# 执行重命名
foreach ($old in $renameMap.Keys) {
    $new = $renameMap[$old]
    if (Test-Path $old) {
        Rename-Item -Path $old -NewName $new
        Write-Host "✅ Renamed: $old -> $new"
    } else {
        Write-Host "❌ Not found: $old"
    }
}
```

保存为 `rename-angry.ps1`，右键 → **使用 PowerShell 运行**

---

## 📊 建议的处理顺序

按照使用频率和重要性排序：

### 第一优先级 (最常用，先处理)
1. ✨ **happy** (31张) - 开心表情最常用
2. ✨ **angry** (76张) - 生气表情也很常用
3. ✨ **sad** (27张) - 伤心表情
4. ✨ **shy** (43张) - 害羞表情

### 第二优先级 (中等使用频率)
5. **confused** (30张)
6. **surprised** (28张)
7. **see** (27张)
8. **like** (15张)

### 第三优先级 (较少使用)
9. **sigh** (14张)
10. **sleep** (8张)
11. **fool** (7张)
12. **morning** (7张)
13. **givemoney** (6张)
14. **baka** (5张)
15. **meow** (5张)
16. **work** (1张)
17. **reply** (1张)

### 第四优先级 (特殊分类)
18. **color** (46张) - 可能不需要重命名
19. **cpu** (21张)
20. **fluxgen** (3张)

---

## 💡 高效技巧

### 1. 分批处理
- 每天处理 1-2 个分类
- 不要急于一次性完成
- 保持命名一致性

### 2. 建立命名模板
为每个分类建立一个**常用词汇表**，重复使用：
```
angry-yelling-01, angry-yelling-02, angry-yelling-03
angry-shouting-01, angry-shouting-02
angry-furious-01, angry-furious-02
```

### 3. 使用编号系统
- 相似的表情用连续编号
- 例如: 3张"微笑"表情 → `happy-smile-01.jpg`, `happy-smile-02.jpg`, `happy-smile-03.jpg`

### 4. 预览图片
- 在 Windows 资源管理器中切换到**大图标**视图
- 或使用 **Windows 照片查看器**批量浏览
- 确保文件名和内容匹配

---

## ✅ 重命名完成后

1. **检查**: 确保没有重复的文件名
2. **测试**: 随机打开几个文件，确认扩展名正确
3. **通知浮浮酱**: 告诉我你完成了哪些分类
4. **重新生成系统**: 浮浮酱会帮你重新生成表情包列表和库

---

## ❓ 常见问题

### Q: 我不知道图片内容是什么怎么办？
A: 打开图片预览，根据视觉判断。实在不确定就用通用词汇，如 `angry-face-01.jpg`

### Q: 文件名太长怎么办？
A: 简化动作词，例如:
- `angry-extremely-furious-yelling` → `angry-furious`
- `happy-very-excited-jumping` → `happy-excited`

### Q: 如果两张图片几乎一样？
A: 使用编号区分:
- `angry-yelling-01.jpg`
- `angry-yelling-02.jpg`

### Q: 可以保留部分原始文件名吗？
A: 不推荐，因为原始文件名没有语义。但如果你想保留编号，可以这样:
- `angry-1739433376.png` (不推荐)
- `angry-yelling-01.png` ✅ (推荐)

---

## 🎉 示例：angry 分类重命名

### 重命名前:
```
0FFD1AFA5CD0866B1065AEAF45D4066A.jpg
1739433376_1.png
1739433584_1.jpg
1739433775_1.jpg
```

### 重命名后:
```
angry-yelling-01.jpg
angry-furious-02.png
angry-mad-03.jpg
angry-upset-04.jpg
```

---

## 📞 需要帮助?

随时告诉浮浮酱你的进度和遇到的问题喵～ (◡‿◡✿)

浮浮酱会在你完成后帮你:
1. 重新生成表情包列表 (.txt)
2. 重新生成表情包库 (emoticon_library.json)
3. 更新 config.env 的提示词
4. 测试表情包功能

加油喵～ φ(≧ω≦*)♪
