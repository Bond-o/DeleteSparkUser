#!/usr/bin/env python3
#deleteUserExample.py

__author__ = "Mike Bond"

'''
    This is an example of using the Requests
    library to delete a user from Cisco Spark
    and then print out the result.

    API Documentation located at the following:
    https://developer.ciscospark.com/endpoint-people-personId-delete.html

'''
import requests

def setHeader():
    """
    A function used to capture the Cisco Spark Token and
    return it's value within the 'spark_header'.
    :return: spark_header:
    """
    count = 0
    """ Loop up to three times to obtain Cisco Spark Token input """
    while True:
        myToken = input('Please enter your Cisco Spark Token: ')
        if not myToken:
            print('\nCisco Spark Token not entered!')
            print('Please try again.\n')
            count = count + 1
            if count < 3:
                continue
            else:
                print('Too many attempts!')
                exit()
        else:
            myToken = 'Bearer ' + myToken
            spark_header = {'Authorization': myToken, 'Content-Type': 'application/json; charset=utf-8'}
            return (spark_header)
            break

def deletePerson(sparkHeader):
    """
    A function used to delete the Cisco Spark User.
    :param sparkHeader:
    :return:
    """
    """ Check that the personID input is not null or less than 79 characters """
    ### Note: as of 04/08/2017, personID equals 79 characters ###
    personID = input('Please enter the Spark Person ID: ')
    if not personID or len(personID) < 79:
        print('\nPlease see the following link on obtaining the Cisco Spark id:')
        print('\thttps://developer.ciscospark.com/endpoint-people-get.html')
        exit()
    else:
        url = 'https://api.ciscospark.com/v1/people/{0}'.format(personID)
        serverRequest = requests.delete(url = url, headers = sparkHeader)
        """ Response Code 204 (Member Deleted) """
        print(serverRequest.status_code, serverRequest.headers)

header = setHeader()
deletePerson(header)
