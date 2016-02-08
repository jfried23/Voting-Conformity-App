import flask
import simplejson
import urllib2

app = flask.Flask( __name__ )
api_key = '1aa8571add7632b2a98c8606c74cdf08:18:25790399'



def fetch_data(gbl_chamber,gbl_congress):
  url='http://api.nytimes.com/svc/politics/v3/us/legislative/congress/%s/%s/members.json?&api-key=%s' %(gbl_congress, gbl_chamber, api_key)
  return simplejson.loads( urllib2.urlopen( url ).read())['results'][0]['members']



@app.route('/index', methods=['POST','GET'])
def run_index():
  if flask.request.method == 'GET':


    gbl_chamber = 'Senate'
    gbl_congress= 113
    gbl_data = fetch_data(gbl_chamber,gbl_congress)

    return flask.render_template('index.html', data=simplejson.dumps(gbl_data), chamber=gbl_chamber.title(), session=gbl_congress )

  elif flask.request.method == 'POST':
    gbl_chamber = flask.request.form['chamber']
    gbl_congress= flask.request.form['con_num']
    gbl_data = fetch_data(gbl_chamber,gbl_congress)



    return flask.render_template('index.html', data=simplejson.dumps(gbl_data), chamber=gbl_chamber.title(), session=gbl_congress )


if __name__ == '__main__':


  app.run( debug=True )
