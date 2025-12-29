"""
VS Code Pylance 集成配置

对应文档: 17-type-system-checkers.md § 17.pyright
"""

# 在 .vscode/settings.json 中添加如下配置：

VSCODE_SETTINGS = """
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.inlayHints.functionReturnTypes": true,
  "python.analysis.inlayHints.variableTypes": true
}
"""

if __name__ == '__main__':
    print("开启 inlayHints (内联提示) 可以让你在没有写类型注解的地方，")
    print("直接在编辑器看到 Pylance 推断出的类型，非常方便。")
