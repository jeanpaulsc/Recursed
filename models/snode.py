# coding: utf8
db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
'''
this table functions to retain both the problem text, likely 
accompanied by an image directly from the book, hand-out etc.

'''
db.define_table('problem',
                Field('probName', 'text'),
                Field('chapter', 'integer'),
                Field('problem', 'integer'),
                Field('image_id', 'reference image'),
                Field('probText', 'text'),
                Field('image_s', 'reference image'),
                Field('solution', 'text'),
                Field('status', 'text'),
                Field('source', 'text'),
                Field('comments', 'text'),
                format = '%(problem)s'))

db.define_table('progress',
                Field('problem_id', 'integer', reference problem),
                Field('type', 'text'),
                Field('body', 'text'),
                Field('comments', 'text'),
				Field('created_by'),
				Field('created_on'))

db.define_table('snode',
				Field('parent_id', reference self),
				Field('root', 'integer'),
				Field('title'),
				Field('body', text))

db.problem.title.requires = IS_NOT_IN_DB(db, 'page.title')
db.problem.body.requires = IS_NOT_EMPTY()
db.problem.solution.readable = db.page.solution.writable = False
##db.problem.created_on.readable = db.page.created_on.writable = False

db.progress.body.requires = IS_NOT_EMPTY()
db.progress.problem_id.readable = db.post.page_id.writable = False
db.progress.created_by.readable = db.post.created_by.writable = False
db.progress.created_on.readable = db.post.created_on.writable = False

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)