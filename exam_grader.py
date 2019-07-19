#!/usr/bin/env python
# coding: utf-8

# # Lab assignment 3 : 학점 계산기

# # 1.

# In[1]:


# 총 과목 수를 Console를 통해 받기
def get_number_of_subjects():

    # """
    # Input:
    # 	- None
    # Output:
    # 	- number_of_subjects: Integer Type의 총 과목 수
    # Examples(python shell):
    # 	>>> import exam_grader as eg
    # 	>>> eg.get_number_of_subjects()
    #   과목수를 입력하세요: 10
    #   10
    # """
    #
    # ===Modify codes below=================
    number_of_subjects = int(input("과목수를 입력하세요."))
    # ======================================
    return(number_of_subjects) # return을 하니까 이 함수를 부르면 줄 것 



# Help Funtion - 수정하지 말 것
def sum_of_scores(number_of_subjects):

    total_score = 0
    for i in range(number_of_subjects):
        message = str(i + 1) + "번째 과목의 점수를 입력하세요 : "
        score = int(input(message))
        total_score = total_score + score
    return(total_score)


# # 3.  Help function - 수정하지 말것, but 다음 시간에 배울 if문에 대해서 적혀 있으므로, 숙제 제출 후 '꼭' 살펴볼 것을 권장합니다.

# In[6]:



#print_exam_garde(average_score)는 성적의 평균값을 바탕으로, '최종'평균과 '학점'을 화면에 '출력'해주는 함수를 사용하는 코드.
#역시 helper 함수로, 수강자가 수정할 필요가 없습니다.
# 그러나, 다음 시간에 배울 if 문에 대해서 적혀 있으므로, 숙제 제출 후 꼭 살펴볼 것을 권장합니다.

# Help Funtion - 수정하지 말 것
def print_exam_grader(average_score):
    grade = 'F'
    if average_score >= 90.0:
        grade = 'A'
    elif average_score >= 80.0:
        grade = 'B'
    elif average_score >= 70.0:
        grade = 'C'
    elif average_score >= 60.0:
        grade = 'D'
    else:
        grade = 'F'
    print("평균 점수: ", average_score)
    print("학     점: ", grade)


# In[7]:


# get_average_score 함수 만들어야함 - 직접 작성 


# # 4. get_average_score
# # input(argument): 1.total_score: Integer Type의 성적 총합, 2. number_of_subjects: Integer Type의 과목 갯수
# # output(return): Float Type의 total_score을 number_of_subjects로 나눈 값

# In[8]:


# Q: return 값과 print의 차이, return까지만 하면 뭐만 됨? 객체나 변수로 저장은 안되던데,


# In[9]:


def get_average_score(total_score,number_of_subjects):
    average_score=total_score/number_of_subjects #return과 print의 차이?
    return average_score #(total_score/number_of_subjects)


# In[10]:


def get_average_score(total_score,number_of_subjects):
    average_score=total_score/number_of_subjects #return과 print의 차이?
    return average_score


# # 5. 이건 뭐하는 코드지? 

# In[11]:


# 처음 두 줄과 마짐가 두 줄은 , 프로그램의 시작과 끝을 알리는 print문으로,
# 실제 프로그램 실행에 영향을 주지 않는다.

def main():
    print("Start of Exam Grader Program")
    print("============================")

    number_of_subjects = get_number_of_subjects() #첫 번째로 수정해야 할 함수가 나옴. - get_number_of_subjectes의 output값을 #number_of_subjects 
    # 변수에 저장하라는 의미 ; get_number_of_subjects는 사용자에게 입력을 받아, '총 과목의 수'를 계산해줌.
    
    # 안해도 됨
    total_score = sum_of_scores(number_of_subjects) # 실제 이번 숙제에 직접ㅈ거인 영향을 주지 않는 helper 함수
    
    
    # 이번 과제에서 갖아 중요한 코드. - 3. 에서 직접 작성이 필요한 함수
    # get_average_score라는 함수에, total_score와 number_of_subjects라는 변수를 입력하여,
    # 성적의 평균값을 average_score에 할당함.
    # number_of_subjects : 첫 번째 코드에서 결정,
    # total_ socre : 두 번째 코드에서 각각 값이 결정됨.
    average_score = get_average_score(
        total_score=total_score, number_of_subjects=number_of_subjects)
   
    #print_exam_garde(average_score)는 성적의 평균값을 바탕으로, '최종'평균과 '학점'을 화면에 '출력'해주는 함수를 사용하는 코드.
    #역시 helper 함수로, 수강자가 수정할 필요가 없습니다.
    # 그러나, 다음 시간에 배울 if 문에 대해서 적혀 있으므로, 숙제 제출 후 꼭 살펴볼 것을 권장합니다.
    print_exam_grader(average_score)

    print("===========================")
    print("End of Exame Grader Program")

if __name__ == '__main__':
    main()


# ### Chap4에서 Conditon 배우면 비슷한거 함
