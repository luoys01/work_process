import datetime
import time

def progress_bar(start_time, end_time, current_time):
    total_seconds = (end_time - start_time).total_seconds()  # 计算总秒数
    elapsed_seconds = (current_time - start_time).total_seconds()  # 计算已过去的秒数
    remaining_seconds = total_seconds - elapsed_seconds  # 计算剩余的秒数

    while remaining_seconds > 0:
        percentage = int((elapsed_seconds / total_seconds) * 100)  # 计算已过去时间的百分比
        progress = '[' + '=' * (percentage // 2) + ' ' * (50 - percentage // 2) + ']'  # 根据百分比生成进度条
        remaining_time = int(remaining_seconds)  # 将剩余秒数转换为整数
        print(f'{progress} {percentage}% (剩余时间: {remaining_time}秒)'.ljust(70), end='\r', flush=True)  # 打印进度条和剩余时间
        time.sleep(0.1)  # 等待0.1秒

        elapsed_seconds += 0.1  # 更新已过去的秒数
        remaining_seconds -= 0.1  # 更新剩余的秒数

    print('[=' * 50 + '] 100%')  # 显示进度条达到100%

# 获取上班时间
start_time_str = input('请输入上班时间（格式为HH:MM）：')
start_time = datetime.datetime.strptime(start_time_str, '%H:%M')

# 获取下班时间
end_time_str = input('请输入下班时间（格式为HH:MM）：')
end_time = datetime.datetime.strptime(end_time_str, '%H:%M')

# 获取当前时间
current_time_str = input('请输入当前时间（格式为HH:MM）：')
current_time = datetime.datetime.strptime(current_time_str, '%H:%M')

# 获取今天的日期
today = datetime.date.today()

# 创建完整的日期时间对象
start_datetime = datetime.datetime.combine(today, start_time.time())
end_datetime = datetime.datetime.combine(today, end_time.time())
current_datetime = datetime.datetime.combine(today, current_time.time())

# 调用进度条函数开始倒计时
progress_bar(start_datetime, end_datetime, current_datetime)
