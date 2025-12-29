"""
Python 3.12+ 类型系统综合应用

对应文档: 14-type-system-basics.md § 14.new
"""

# 1. 定义领域特定的类型别名
type UserId = int
type Email = str
type PhoneNumber = str
type Timestamp = float

# 2. 定义联合类型别名
type ContactInfo = Email | PhoneNumber

# 3. 定义泛型响应结构
type Response[T] = tuple[bool, T | None, str]

# 4. 泛型仓库接口模拟
class Repository[T]:
    def __init__(self):
        self._storage: dict[int, T] = {}
        self._next_id: int = 1
        
    def add(self, item: T) -> int:
        item_id = self._next_id
        self._storage[item_id] = item
        self._next_id += 1
        return item_id
    
    def get(self, item_id: int) -> T | None:
        return self._storage.get(item_id)

# 5. 业务模型
type UserData = dict[str, str | int | bool]

def create_user(
    name: str,
    contact: ContactInfo,
    repo: Repository[UserData]
) -> Response[UserId]:
    """创建用户的业务逻辑"""
    
    # 验证联系方式 (模拟)
    if not contact:
        return False, None, "Invalid contact info"
    
    user_data: UserData = {
        "name": name,
        "contact": contact,
        "active": True
    }
    
    uid = repo.add(user_data)
    return True, uid, "User created successfully"

if __name__ == '__main__':
    # 初始化仓库
    user_repo = Repository[UserData]()
    
    # 执行业务逻辑
    success, uid, msg = create_user(
        name="Alice",
        contact="alice@example.com",
        repo=user_repo
    )
    
    if success and uid is not None:
        print(f"Success! User ID: {uid}, Message: {msg}")
        # 从仓库获取数据
        saved_user = user_repo.get(uid)
        print(f"Saved data: {saved_user}")
    else:
        print(f"Failed! Message: {msg}")
