

function fuzzyPlural(single) {
print("EE: "+single);
  //var result = single.replace(/o/g, 'e');  
  var result = single;
  if( single === 'kangaroo'){
    result += 'se';
  }
  return '<'+result+'>'; 
}

var words = ["foot", "goose", "moose", "kangaroo"];
print(words.map(fuzzyPlural));

// ["feet", "geese", "meese", "kangareese"]

/*
=!EXPECTSTART!=
EE: foot
EE: goose
EE: moose
EE: kangaroo
[ "<foot>", "<goose>", "<moose>", "<kangaroose>" ]
=!EXPECTEND!=
*/
