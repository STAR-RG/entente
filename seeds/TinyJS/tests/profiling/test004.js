// naive smoothing

function smooth(image) {
	var output = [];
	var image_length = image.length;
	for(var i = 0; i < image_length; i++) {
		output[i] = [];
		var ii_max = i+1 < image[i].length ? i+1 : image[i].length;
		var j_max = image[i].length;
		for(var j = 0; j < j_max; j++) {
			var jj_max = Math.min(j+1, image[i][j].length);
			var result = { r: 0, g: 0, b: 0 };
			for(var ii = Math.max(0, i-1); ii < ii_max; ii++) {
				for(var jj = Math.max(0, j-1); jj < jj_max; jj++) {
					result.r += image[i][j].r;	
					result.g += image[i][j].g;
					result.b += image[i][j].b;
				}
			}
			result.r = result.r / 9;	  
			result.g = result.g / 9;
			result.b = result.b / 9;
			output[i][j] = result;
		}
	}
	return output;
}

function init() {
	NUM_ITERATIONS = 2;
	IMAGE_WIDTH = 100;
	IMAGE_HEIGHT = 100;
}

function create() {
	var output = [];
	for(var i = 0; i < IMAGE_WIDTH; i++) {
		output[i] = [];
		for(var j = 0; j < IMAGE_HEIGHT; j++)
			output[i][j] = {
				r: Math.randInt(0, 255),
				g: Math.randInt(0, 255),
				b: Math.randInt(0, 255)
			};
	}
	return output;
}

function get_iterations() { return NUM_ITERATIONS; }
function get_arg_list() { return "IMAGE"; }
function get_function_name() { return "smooth"; }

function setup() {
    IMAGE = create();
}