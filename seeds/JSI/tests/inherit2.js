

var john = {firstName: 'John', lastName: 'Smith'};
var jane = {firstName: 'Jane'};
Object.setPrototypeOf(jane, john);
print("LN:="+jane.lastName);
jane.lastName = 'Doe';
print("LN2:="+jane.lastName);
print("LN3:="+john.lastName);
delete jane.lastName;
print("LN4:="+jane.lastName);

/*
=!EXPECTSTART!=
LN:=Smith
LN2:=Doe
LN3:=Smith
LN4:=Smith
=!EXPECTEND!=
*/
