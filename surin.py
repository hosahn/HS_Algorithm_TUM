print("박수린 테스트! 아무 키나 입력하세요!")

dummy = input()
score = 0
print("고양이를 좋아하면 1번, 강아지를 좋아하면 2번")

animal = int(input())

if(animal == 1) :
    score += 2

print("해산물을 좋아하면 1번, 아니면 2번")

food = int(input())

if(food == 1) :
    score += 2

print("이호산을 사랑하면 1번 아니면 2번")

love = int(input())

if(love != 1) :
    print("당신은 절대 박수린일 수가 없습니다.")
else :
    score += 2
    print("만사가 귀찮으면 1번 아니면 2번")
    lazy = int(input())
    if(lazy == 1) :
        score += 2
    print("양주가 좋으면 1번, 소주나 전통주가 좋으면 2번")
    drink = int(input())
    if(drink == 1) :
        score += 2
    print("잘생김 1번, 듬직함 2번")
    a = int(input())
    if(a == 2) :
        score += 2
    result = str(score)
    print("당신의 점수는 " + result

          + "점입니다. 따라서 당신은!")
    if (score >= 12) :
        print("박수린입니다,")
    elif (score <= 8) :
        print("조금 애매한 박수린입니다.")
    elif (2 < score and score <= 4) :
        print("글쎄..수린이 아닌것같은데..")
    else :
        print("너 누구야!!")