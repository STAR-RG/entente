var re;
var t;

/*===
2
8
===*/

/* Test that lastIndex is correct (in characters) even for a non-ASCII string. */

re = /foo(...)/g;
t = re.exec('\u1234\uabcdfoo\u4321\u1234\u4321quux');
print(t.index);
print(re.lastIndex);

/* XXX: non-ascii values for every operator */
/* XXX: add more cases */
