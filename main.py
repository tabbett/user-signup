

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import re

form = """
<form method = "post">
    <label>
        <h3>Username
        <textarea name = 'username' value = "%(username)s"> 
        </textarea>
        <div style ="color: red">%(username_error)s</div>              
        </h3>
    </label>

    <label>
        <h3>Password
        <textarea name = 'password' type = "password">
        </textarea> 
        <div style ="color: red">%(password_error)s</div>
        </h3>
    </label>

    <label>
        <h3>Verify Password
        <textarea name = 'verify' type = "password">
        </textarea> 
        <div style ="color: red">%(verification_error)s</div>
        </h3>
    </label>

    <label>
        <h3>Email (optional)
        <textarea name = 'email' value ="%(email)s">
        </textarea> 
         <div style ="color: red">%(email_error)s</div>
        </h3>
    </label>
    <br>
    <input type = submit>

</form>
"""

header = "<h1>Signup </h1><br>"


password_re = re.compile(r"^.{3,20}$")
email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(user):
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(user) 

def valid_password(password):
    return password_re.match(password)

def valid_email(email):
    return email_re.match(email)

class MainHandler(webapp2.RequestHandler):
   
    def write_form(self, username="", username_error="", password_error="", 
                    verification_error="", email="", email_error=""):
        values = {
            "username": username,
            "username_error": username_error,
            "password_error": password_error,
            "verification_error": verification_error,
            "email": email,
            "email_error": email_error

        }
        
        response = form %(values)
        self.response.out.write(header + response)
    
    def get(self):
        self.write_form()

    def post(self):
        user = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        if valid_username(user):
            self.response.write("Welcome, " + user +"!")
        else:
            username_error = "That's not a valid username"
            self.write_form(username = user, username_error = username_error)

            
       # elif not password or not valid_password(password):
       #     password_error = "That wasn't a valid password"
       #     self.response.write(form)
       # elif password != verify:
       #     verification_error = "Your passwords didn't match"
       # elif not valid_email(email):
       #     email_error = "That's not a vaild email"
#class WelcomeHandler(webapp2.RequestHandler):

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


