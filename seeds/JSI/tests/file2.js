

File.mkdir('XX1');
File.mkdir('XX1/AA');
File.mkdir('XX1/BB');
File.rename('XX1/BB','XX1/CC.txt');
print(File.glob(null,{dir:'XX1'}).sort());
print(File.dirname('XX1/AA'));
print(File.rootname('XX1/CC.txt'));
print(File.tail('XX1/CC.txt'));
print(File.type('XX1/CC.txt'));
print(File.extension('XX1/CC.txt'));
//print(File.realpath('XX1/CC.txt'));
print(File.writable('XX1/CC.txt'));
print(File.readable('XX1/CC.txt'));
print(File.exists('XX1/CC.txt'));
print(File.isdir('XX1/CC.txt'));
print(File.isfile('XX1/CC.txt'));
File.remove('XX1',true);

/*
=!EXPECTSTART!=
[ "AA", "CC.txt" ]
XX1
XX1/CC
CC.txt
directory
.txt
true
true
true
true
false
=!EXPECTEND!=
*/
