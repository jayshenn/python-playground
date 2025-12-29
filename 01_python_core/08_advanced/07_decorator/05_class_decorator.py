"""
类装饰器

对应文档: 10-advanced-features.md § 10.7.5
"""

# 类装饰器主要依赖 __call__ 魔法方法，使得实例对象可以像函数一样被调用

class CheckPermission:
    def __init__(self, func):
        self.func = func
        self.is_admin = True # 模拟权限状态

    def __call__(self, *args, **kwargs):
        if self.is_admin:
            print("[权限检查] 验证通过")
            return self.func(*args, **kwargs)
        else:
            print("[权限检查] 权限不足！")

@CheckPermission
def delete_user(user_id):
    print(f"用户 {user_id} 已删除")

if __name__ == '__main__':
    delete_user(101)
