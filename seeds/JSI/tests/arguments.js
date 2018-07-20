

var i;
function a() {
	for (i = 0; i < arguments.length; ++i) {
		print(arguments[i]);
	}
};

a(1,2,3,4,"xfsldafkjasldf","asdfsadfsadf");
print(i);

/*
=!EXPECTSTART!=
1
2
3
4
xfsldafkjasldf
asdfsadfsadf
6
=!EXPECTEND!=
*/
