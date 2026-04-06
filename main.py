import json

def print_menu():
    print("========================================")
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")
    input("선택 : ")

def main():
    menu = print_menu()
    menu = int(number)

    if menu == 1:
        play_quiz()
    elif menu == 2:
        plus_quiz()
    elif menu == 3:
        quiz_list()
    elif menu == 4:
        check_score()
    elif menu == 5:
        exit


if __name__ == "__main__":
    main()