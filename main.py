# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    total = sum(range(1, 11))
    print(f'1到10的总合为: {total}')
    numbers = list(range(1, 11))
    for num in numbers:
        print(num)

    import random
    names = ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九', '吴十', '郑十一', '王十二']
    genders = ['男', '女']
    occupations = ['工程师', '教师', '医生', '律师', '会计', '设计师', '销售', '经理']
    Persons = []
    for i in range(10):
        age = random.randint(18, 70)
        if age < 18:
            age_group = '青年'
        elif age <= 59:
            age_group = '中年'
        else:
            age_group = '老年'
        person = {
            '姓名': names[i],
            '性别': random.choice(genders),
            '年龄': age,
            '职业': random.choice(occupations),
            '年龄段': age_group
        }
        Persons.append(person)
    for p in Persons:
        print(f"姓名: {p['姓名']}, 性别: {p['性别']}, 年龄: {p['年龄']}, 职业: {p['职业']}, 年龄段: {p['年龄段']}")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
