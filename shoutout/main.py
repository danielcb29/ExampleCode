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
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp \
	import template

class Shout(db.Model):
	message = db.StringProperty(required=True)

	when = db.DateTimeProperty(auto_now_add=True)

	who = db.StringProperty()

class MyHandler(webapp.RequestHandler):
    def get(self):
    	shouts = db.GqlQuery(
    		'SELECT * FROM Shout ' 
    		'ORDER BY when DESC')
    		#'ORDER BY when DESC')
    	values = {
    		'shouts': shouts	
    	}
        self.response.write(template.render('main.html',values))
        #self.response.write('Hello!!')
    def post(self):
    	shout = Shout(message=self.request.get('message'),who=self.request.get('who'))
    	shout.put()
    	self.redirect('/')
    	#self.response.out.write("Posted!!")

#def main():
app = webapp.WSGIApplication([
    (r'.*', MyHandler)
], debug=True)
#	wsgiref.handlers.CGIHandler().run(app)

#if __name__ == "__main__":
#	main()
