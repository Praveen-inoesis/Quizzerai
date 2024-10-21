#organization
{
  "organization_name": "string",
  "organization_id": "string",
  "domain_name": "string",
  "admin_email": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "disable": "boolean",
  "logo": "string", 
  "is_active": "boolean", 'allow null' #update later
  "subscription_plan": "string", 'allow null' #update later
  "subscription_start_date": "datetime", 'allow null' #update later
  "subscription_end_date": "datetime", 'allow null' #update later
  "address": {
    "street": "string",
    "city": "string",
    "state": "string",
    "country": "string",
    "postal_code": "string",
    "phone_number":"string"
  }
}


# Question bank

 # "owner": {
  #   "user_id": 2,
  #   "username": "jane_smith"
  # },
{
 
  "question_banks": [
    {
      "question_banks_id": 1,
      "name": "Geography Questions",
      "description": "A collection of geography-related questions.",
      "question_type": [
        {
          "question_type": 1,
          "name": "Multiple Choice",
          "questions": [
            {
              "question_id": 1,
              "question_text": "What is the capital of France?",
              "choices": {
                "A": "Berlin",
                "B": "Madrid",
                "C": "Paris",
                "D": "Rome"
              },
              "correct_answer": "C"
            },
            {
              "question_id": 2,
              "question_text": "Which is the longest river in the world?",
              "choices": {
                "A": "Amazon River",
                "B": "Nile River",
                "C": "Yangtze River",
                "D": "Mississippi River"
              },
              "correct_answer": "B"
            },
            {
              "question_id": 3,
              "question_text": "Which continent is the Sahara Desert located in?",
              "choices": {
                "A": "Asia",
                "B": "North America",
                "C": "Africa",
                "D": "Australia"
              },
              "correct_answer": "C"
            }
          ]
        },
       
        {
          "question_type": 2,
          "name": "Match the Following",
          "questions": [
            {
              "question_id": 1,
              "question_text": "Match the following countries with their capitals.",
              "match_the_following": {
                "USA": "New Delhi",
                "UK": "Washington, D.C.",
                "India": "London"
              },
              "correct_answer": {
                "USA": "Washington, D.C.",
                "UK": "London",
                "India": "New Delhi"
              }
            },
            {
              "question_id": 2,
              "question_text": "Match the following Indian states with their languages.",
              "match_the_following": {
                "Delhi": "Malayalam",
                "Kerala": "Hindi",
                "Tamilnadu": "Telugu",
                "Karnataka": "Tamil"
              },
              "correct_answer": {
                "Delhi": "Hindi",
                "Kerala": "Malayalam",
                "Tamilnadu": "Tamil",
                "Karnataka": "Telugu"
              }
            }
          ]
        }
      ]
    }
  ]
}

{
 
  "question_banks": [
    {
      "question_banks_id": 1,
      "name": "Geography Questions",
      "description": "A collection of geography-related questions.",
      "question_type": [
        {
          "question_type": 1,
          "name": "Multiple Choice",
          "questions": [
            {
              "question_id": 1,
              "question_text": "What is the capital of France?",
              "choices": {
                "A": "Berlin",
                "B": "Madrid",
                "C": "Paris",
                "D": "Rome"
              },
              "correct_answer": "C"
            },
            {
              "question_id": 2,
              "question_text": "Which is the longest river in the world?",
              "choices": {
                "A": "Amazon River",
                "B": "Nile River",
                "C": "Yangtze River",
                "D": "Mississippi River"
              },
              "correct_answer": "B"
            },
            {
              "question_id": 3,
              "question_text": "Which continent is the Sahara Desert located in?",
              "choices": {
                "A": "Asia",
                "B": "North America",
                "C": "Africa",
                "D": "Australia"
              },
              "correct_answer": "C"
            }
          ]
        },
       
        {
          "question_type": 2,
          "name": "Match the Following",
          "questions": [
            {
              "question_id": 1,
              "question_text": "Match the following countries with their capitals.",
              "match_the_following": {
                "USA": "New Delhi",
                "UK": "Washington, D.C.",
                "India": "London"
              },
              "correct_answer": {
                "USA": "Washington, D.C.",
                "UK": "London",
                "India": "New Delhi"
              }
            },
            {
              "question_id": 2,
              "question_text": "Match the following Indian states with their languages.",
              "match_the_following": {
                "Delhi": "Malayalam",
                "Kerala": "Hindi",
                "Tamilnadu": "Telugu",
                "Karnataka": "Tamil"
              },
              "correct_answer": {
                "Delhi": "Hindi",
                "Kerala": "Malayalam",
                "Tamilnadu": "Tamil",
                "Karnataka": "Telugu"
              }
            }
          ]
        }
      ]
    }
  ]
}



# {
#           "question_type_id": 4,
#           "name": "Spot the Error",
#           "questions": [
#             {
#               "question_id": 1,
#               "question_text": "The capital of France is Madrid.",
#               "correct_answer": "The capital of France is Paris, not Madrid."
#             },
#             {
#               "question_id": 2,
#               "question_text": "Water boils at 90 degrees Celsius.",
#               "correct_answer": "Water boils at 100 degrees Celsius, not 90."
#             },
#             {
#               "question_id": 3,
#               "question_text": "There are 50 days in a month.",
#               "correct_answer": "A month has 30 or 31 days, not 50."
#             }
#           ]
#         },
#          


#response
{
  "id": 14,  #question id its auto generate
  "question_text": "The Pacific Ocean is the largest ocean on Earth.",   
  "correct_answer": "True",
  "question_type": 3
}

#request
{
  "question_type": 3, 
  "question_text": "The Pacific Ocean is the largest ocean on Earth.",
  "correct_answer": "True" 
}







{
          "question_type_id": 3,
          "name": "True or False",
          "questions": [
            {
              "question_id": 1,
              "question_text": "The Pacific Ocean is the largest ocean on Earth.",
              "correct_answer": "True"
            },
            {
              "question_id": 2,
              "question_text": "Australia is the smallest continent in the world.",
              "correct_answer": "True"
            },
            {
              "question_id": 3,
              "question_text": "The Indian Ocean is the largest ocean on Earth.",
              "correct_answer": "False"
            }
          ]
        }