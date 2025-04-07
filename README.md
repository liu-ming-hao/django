# 会议室管理系统

这是一个基于Django框架开发的会议室管理系统，主要用于管理面试和会议室的预约。

## 项目结构

```
meetingroom/
├── interview/          # 面试管理应用
│   ├── admin.py       # 管理后台配置
│   ├── models.py      # 数据模型定义
│   ├── views.py       # 视图函数
│   ├── dingtalk.py    # 钉钉集成
│   └── candidate_field.py  # 候选人字段定义
├── jobs/              # 职位管理应用
│   ├── admin.py       # 管理后台配置
│   ├── models.py      # 数据模型定义
│   ├── views.py       # 视图函数
│   └── templates/     # 模板文件
├── settings/          # 项目配置
│   ├── base.py        # 基础配置
│   └── local.py       # 本地环境配置
└── manage.py          # Django管理脚本
```

## 主要功能

1. 面试管理
   - 候选人信息管理
   - 面试预约
   - 钉钉集成

2. 职位管理
   - 职位信息维护
   - 职位发布
   - 职位申请管理

3. 会议室管理
   - 会议室预约
   - 会议室使用状态跟踪

## 技术栈

- Python 3.x
- Django
- SQLite
- 钉钉API集成

## 安装和运行

1. 克隆项目
```bash
git clone [项目地址]
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 数据库迁移
```bash
python manage.py migrate
```

4. 运行开发服务器
```bash
python manage.py runserver
```

## 环境要求

- Python 3.x
- Django 3.x
- 其他依赖见 requirements.txt

## 配置说明

项目使用多环境配置：
- base.py: 基础配置
- local.py: 本地开发环境配置

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 版本
git config --global --add safe.directory 


## 许可证

[许可证类型] 