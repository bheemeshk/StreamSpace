from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# Classes for CRUD Ops
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# CONNECT TO DATABASE
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:

            # LISTING NEW RESTAURANTS
            if self.path.endswith("/restaurants"):

                # Get restaurant Names to list all the names
                restaurantNames = session.query(Restaurant).all()

                # CONSTRUCT HTML
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()
                output=""
                output += "<html><body><h2>Restaurant Names</h2>"
                output += "<a href='/restaurants/new'> Create New Restaurant </a></br></br>"
                # Iterate and add the restaurant names to HTML
                for res in restaurantNames:
                    output += "%s  " % res.name
                    output += "<a href='/restaurants/%s/edit'> EDIT </a>" % res.id
                    output += "<a href='/restaurants/%s/delete'>DELETE</a> </br>" % res.id


                output += "</body></html>"
                self.wfile.write(output)
                print output
                return





            # CREATING NEW RESTAURANTS
            if self.path.endswith("/restaurants/new"):

                # Get restaurant Names to list all the names
                restaurantNames = session.query(Restaurant).all()

                # CONSTRUCT HTML
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()
                output=""
                output += "<html><body><h2>Create New Restaurant</h2>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>" \
                          "<input name='newRestaurantName' type='text'> " \
                          "<input type='submit' value='Create'>" \
                          "</form>"

                output += "</body></html>"
                self.wfile.write(output)
                print output
                return



            #EDITING A RESTAURANT NAME

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRes = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                if myRes != []:
                    self.send_response(200)
                    self.send_header('content-type','text/html')
                    self.end_headers()

                    output=""
                    output += "<html><body><h2>Create New Restaurant</h2>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % restaurantIDPath
                    output += "<input name='newRestaurantName' type='text' placeholder = %s > " % myRes.name
                    output += "<input type='submit' value='Create'>" \
                              "</form>"

                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return






            #DELETE A RESTAURANT NAME

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRes = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                if myRes != []:
                    self.send_response(200)
                    self.send_header('content-type','text/html')
                    self.end_headers()

                    output=""
                    output += "<html><body><h2>Create New Restaurant</h2>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<h4>Are you sure of deleting %s ?</h4> " % myRes.name
                    output += "<input type='submit' value='delete'>" \
                              "</form>"

                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return


            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()

                output=""
                output += "<html><body>Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                          "<h2>What would you like me to say?</h2>" \
                          "<input name='message' type='text'> " \
                          "<input type='submit' value='submit'>" \
                          "</form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()

                output=""
                output += "<html><body>!Hola!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
                          "<h2>What would you like me to say?</h2>" \
                          "<input name='message' type='text'> " \
                          "<input type='submit' value='submit'>" \
                          "</form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)


    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                newRestaurant = Restaurant(name = messagecontent[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('content_type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()



            # Script to Edit Restauratnt

            if self.path.endswith("/edit"):

                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')
                restaurantIDPath = self.path.split("/")[2]


                resQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                if resQuery != []:
                    resQuery.name = messagecontent [0]
                    session.add(resQuery)
                    session.commit()

                self.send_response(301)
                self.send_header('content_type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()



            #TO DELETE RESTAURANT
            if self.path.endswith("/delete"):
                    print "In Delete do_post"
                    ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]


                    resQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()

                    if resQuery != []:
                        session.delete(resQuery)
                        session.commit()

                    self.send_response(301)
                    self.send_header('content_type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()


            # self.send_response(301)
            # self.end_headers()
            #
            # ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            # if ctype == 'multipart/form-data':
            #     fields=cgi.parse_multipart(self.rfile, pdict)
            #     messagecontent = fields.get('message')
            #
            # output=""
            # output += "<html><body> "
            # output += "<h2>Okay, how about this:</h2>"
            # output += "<h1> %s </h1>" % messagecontent[0]
            #
            #
            # output += "<form method='POST' enctype='multipart/form-data' action='/hello'>" \
            #           "<h2>What would you like me to say?</h2>" \
            #           "<input name='message' type='text'> " \
            #           "<input type='submit' value='submit'>" \
            #           "</form>"
            # output += "</body></html>"
            # self.wfile.write(output)
            # print output
            # return

        except:
            pass

def main():
    try:
        port =8080
        server = HTTPServer(('',port), webserverHandler)
        print "Webserver is running on port %s:" %port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()





if __name__ == "__main__":
    main()