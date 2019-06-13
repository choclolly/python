choice = input('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？\n')
if choice == '不需要':
    print('好的，再见。')
else:
    number1 = int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询\n'))
    if number1 == 1:
        print('小精灵会推荐你去存取款窗')
    elif number1 == 3:
        print('小精灵会推荐你去咨询窗口')
    elif number1 == 2:
        number = int(input('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币 \n小精灵：请问您需要兑换多少金加隆呢？\n'))
        print(('小精灵：好的，我知道了，您需要兑换' + str(number) + '金加隆。'))
        input('小精灵：那么，您需要付给我' + str(number * 51.3) + '人民币。')
        print('程序结束')
