import facebook

idarray = [10153959284770329, 10153961956260329]

graph = facebook.GraphAPI(access_token='<access_token>', version='2.2')
post = graph.get_object(id='10153959284770329/likes?summary=true')
print post['summary']['total_count']
