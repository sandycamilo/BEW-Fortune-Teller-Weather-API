#HW1
##What happens when you press the “submit” button? Paste the full URL you are sent to on submit.

       file:///fortune_results?FirstName=sa&animal=Whale&city1=Seattle

###What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?

       FirstName, animal, city1 - Info being asked from the user. 

##What are the values of the URL query string? How do they correspond to what the user entered or typed?

       sa, Whale, Seattle - Info retrieved from the user. 


#HW3
##Describe the data contained in the API response. What can we discern about the weather in the specified city?
  
      In the API response we can see the coordinates, the temperature(min and max), the visibility, rain, timezone and                sunrise/sunset estimates.  

#How would we obtain the temperature in the specified city? Describe using Python dictionary syntax. (HINT: Assume that the JSON response is stored in a variable called json_response.)

     We access the main field and then temp. The integer is in Kelvin so we would need to convert it before writing our routes.



