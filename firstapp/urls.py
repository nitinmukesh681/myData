from django.conf.urls import url
from firstapp.views import *

urlpatterns = [
	url(r'home/',homepage,name = 'homepage'),
	# url(r'addbook/',addBook,name = 'addbook'),
	# url(r'addAbook/',addAbook,name = 'addAbook'),	
	# url(r'register/',registerYourself,name = 'registerYourself'),
	url(r'loginAcc/',loginAcc,name = 'user_login'),
	url(r'user_logout/',user_logout,name = 'user_logout'),
	url(r'fileUpload/',fileUpload,name = 'fileUpload'),
	# url(r'commentIs/',commentIs,name = 'commentIs'),
	url(r'searchByField/',searchByField,name = 'searchByField'),
	url(r'allData/',allData,name = 'allData'),
	# url(r'uploadNotes/',uploadNotes,name = 'uploadNotes'),
	# url(r'product_details/(?P<name>[\w|\W]+)/(?P<id>\d+)/$',product_details,name = 'product_details'),
	# url(r'product_details_1/',product_details_1,name = 'product_details_1'),
	# url(r'subjectWise/(?P<id>\d+)/$',subjectWise,name = 'subjectWise'),
	# url(r'notes_details/(?P<id>\d+)/$',notes_details,name = 'notes_details'),
	# url(r'addbook/',addbook,name = 'addbook'),
	# url(r'uploadBooks/',uploadDocuments,name = 'uploadBooks'),
	# url(r'subCatgBooks/(?P<id>\d+)/(?P<id1>\d+)/$',subCatgBooks,name = 'subCatgBooks'),
	# url(r'notesCatg/(?P<id>\d+)/$',notesCatg,name = 'notesCatg'),
	# url(r'examCatG/(?P<id>\d+)/$',examCatG,name = 'examCatG'),
	# url(r'entranceCat/(?P<id>\d+)/$',entranceCat,name = 'entranceCat'),
	# url(r'donatebooks/',donatebooks,name = 'donatebooks'),
	# url(r'uploadDonateBooks/',uploadDonateBooks,name = 'uploadDonateBooks'),
	# url(r'uploadDocuments/',uploadDocuments,name = 'uploadDocuments'),
	# url(r'requestShow/',requestShow,name = 'requestShow'),
	# url(r'addRequest/',addRequest,name = 'addRequest'),
	# url(r'SelectedProducts/(?P<name>[\w|\W]+)/(?P<id>\d+)/$',SelectedProducts,name = 'SelectedProducts'),
	# url(r'selectCollege/(?P<name>[\w|\W]+)/(?P<id>\d+)/$',selectCollege,name = 'selectCollege'),
	# url(r'notes_details/(?P<name>[\w|\W]+)/(?P<id>\d+)/$',notes_details,name = 'notes_details'),

	]