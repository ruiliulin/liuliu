from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
llr_survey = AnonymousSurvey(question)

# 显示问题并存储答案
llr_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    r = input("Language:")
    if r == 'q':
        break
    else:
        llr_survey.store_response(r)

# 显示调查结果
llr_survey.show_results()


