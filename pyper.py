##################################
# Date of creation: 07.11.2023
# Programmer: Ondrej Tomasek
# LinkedIn: linkedin.com/in/ondrat
##################################

# Please make sure you have Python 3.0 or higher installed
# Use this library for your personal projects and please link library :)

# GLOBAL IMPORTS
import random
import string
import requests

class API:
    def send_api_request(url, method='GET', data=None, headers=None, params=None):
    """
    Send an API request and return the response.

    Parameters:
    - url (str): The API endpoint URL.
    - method (str): The HTTP method (default is 'GET').
    - data (dict): The data to be sent in the request body (for POST, PUT, etc.).
    - headers (dict): Additional headers to include in the request.
    - params (dict): URL parameters.

    Returns:
    - requests.Response: The response object.
    """
    
    # Choose the appropriate requests method based on the provided HTTP method
    method = method.upper()
    if method not in ['GET', 'POST', 'PUT', 'DELETE']:
        raise ValueError("Invalid HTTP method. Supported methods are GET, POST, PUT, DELETE.")

    # Prepare the request
    if method == 'GET':
        response = requests.get(url, headers=headers, params=params)
    elif method == 'POST':
        response = requests.post(url, headers=headers, json=data, params=params)
    elif method == 'PUT':
        response = requests.put(url, headers=headers, json=data, params=params)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers, params=params)

    # Response from the API
    return response
    
class Generate:

    class Id:
        """
        Generate random ID and get it in INT
        
        Parameters:
        - length - (optional, default=3) Length of ID
        - excluded_numbers - (optional) Numbers in List that you don't want to include in the final ID, input format example: [5, 1, 0]
        CALL EXAMPLE:
        - ID(4, [0, 5])
            + Generates ID which length is 4 and excluded numbers are 0 and 5
        """
        
        @staticmethod
        def ID(length=3, excluded_numbers=[]):

            if len(excluded_numbers) > 9:
                raise ValueError("Excluded too many numbers, ID can not be generated.")
            elif length < 1:
                raise ValueError("Length is set to 0 or negative, ID can not be generated.")

            random_id = ""
            while len(random_id) < length:
                num = str(random.randint(0, 9))
                if num not in map(str, excluded_numbers):
                    random_id += num
            return int(random_id)
            
        """
        Generate multiple random IDs and get them in LIST
        
        Parameters:
        - how_many - (optional, default=3) How many IDs to generate
        - length_of_each_one - (optional, default=3) Length of ID
        - excluded_numbers - (optional) Numbers in List that you don't want to include in the final ID, input format example: [5, 1, 0]
        CALL EXAMPLE:
        - IDs(7, 4, [0, 5])
            + Generates 7 IDs which each length is 4 and excluded numbers are 0 and 5
        """
        
        @staticmethod
        def IDs(how_many=3, length_of_each_one=3, excluded_numbers=[]):

            if how_many < 1:
                raise ValueError("Length is set to 0 or negative, ID can not be generated.")

            ran_ids = []
            for i in range(how_many):
                ran_id = Generate.Id.ID(length_of_each_one, excluded_numbers)
                ran_ids.append(ran_id)
            return ran_ids


    class Password:

        """
        GENERATE RANDOM PASSWORD
        
        Parameters:
        - length - (optional, default=10) Length of password
        - excluded_chars - (optional) Chars in List that you don't want to include in the final password, input format example: ["h", "g", "a"]
        CALL EXAMPLE:
        - Generate.Password.Password(4, ["a", "c"])
            + Generates password with length of 4 and excluded characters "a" and "c"
        """
        
        @staticmethod
        def Password(length=10, excluded_chars=[]):
            try:
                characters = [char for char in string.ascii_letters + string.digits + string.punctuation if
                              char not in excluded_chars]
            except Exception as exception:
                raise ValueError(f"Something went wrong with excluding wanted character. Excluded characters entered:{excluded_chars} and exception: {exception}.")

            if length > len(characters):
                raise ValueError("Password length is too long given the excluded characters.")

            password = ''.join(random.choice(characters) for _ in range(length))

            return password

        """
        GENERATE RANDOM PASSWORDS and GET THEM IN LIST
        
        Parameters:
        - how_many - (optional, default=3) How many Passwords to generate
        - length_of_each_one - (optional, default=10) Length of password
        - excluded_chars - (optional) Chars in List that you don't want to include in the final password, input format example: ["h", "g", "a"]
        CALL EXAMPLE:
        - Generate.Password.Passwords(10, 4, ["a", "c"])
            + Generates 10 random passwords with each length of 4 and excluded characters "a" and "c"
        """

        @staticmethod
        def Passwords(how_many=3, length_of_each_one=10, excluded_chars=[]):

            if how_many < 1:
                raise ValueError("Length is set to 0 or negative, ID can not be generated.")

            pwds = []
            for i in range(how_many):
                pwd = Generate.Password.Password(length_of_each_one, excluded_chars)
                pwds.append(pwd)

            return list(pwds)







