from flask import Flask, json
# flask web framework is useful to lauch quick


app = Flask (__name__) # craete the flask instance


# create the URL route in the application

@app.route ('/total', methods=['GET'])

def get_total():

    total = 0  # Inialise the integer variable to calcualte  the sum value

    num_to_add = list (range (10000001))  # initialise the list ranging. the code can work without the range as list
    #values are fixed.
    num_to_add = [1, 2, 3]  # Hardcoded the list to calculate the fix numbers.

    for num1 in range (0, len (num_to_add)):  # loop through the list upto the hardcoded length of list

        total = total + num_to_add[num1]  # move the next value and add that is 1+2, 1+2+3 and so on if required.

        print ("total is =", total)  # gives the total of every iteration and the toal sum.

    return json.dumps(total) # this allow you to have an output of data in json.
    # other option if you are using a templete then output can be sent to HTML file. in that case output would be total.html


if __name__ == '__main__':

    app.run (debug=True)
    #if you running a standalone mode by default localhost is called.
    #for the specfic address change app run to (host='0.0.0.0',port=5000)
