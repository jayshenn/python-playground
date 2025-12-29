# 序列化与反序列化

Pydantic 不仅擅长验证数据，还能在 Python 对象与各种数据格式（如字典、JSON）之间进行高效转换。

## 目录

- [01_export_dict_json.py - 导出数据](01_export_dict_json.py)：介绍如何使用 `model_dump()` 和 `model_dump_json()` 将模型转换为字典和 JSON 字符串。
- [02_load_from_dict_json.py - 加载数据](02_load_from_dict_json.py)：介绍如何从现有字典或 JSON 字符串安全地还原模型实例。
- [03_exclude_include_fields.py - 包含与排除](03_exclude_include_fields.py)：展示如何在序列化时动态过滤字段（例如隐藏密码或内部 ID）。
- [04_json_schema.py - JSON Schema](04_json_schema.py)：展示如何自动生成符合 JSON Schema 标准的结构定义，用于接口文档或跨语言验证。

## 核心方法

- **model_dump()**：返回一个 Python 字典。
- **model_dump_json()**：返回一个 JSON 字符串，并自动处理日期、UUID 等不可直接序列化的类型。
- **model_validate()**：从字典创建模型。
- **model_validate_json()**：从 JSON 字符串创建模型。

## 学习建议

- 在处理日期时间（`datetime`）时，优先使用 `model_dump_json()`，因为它能自动处理 ISO 格式转换。
- 利用 `exclude` 参数来保护敏感信息，避免在 API 响应中泄露密码哈希等数据。
