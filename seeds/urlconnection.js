importPackage( java.net );

// connect to the remote resource
var u = new URL( "http://www.mozilla.org/news.rdf" );
var c = u.openConnection();
c.connect();

// read in the raw data
var s = new java.io.InputStreamReader( c.getInputStream() );
var b = new java.io.BufferedReader( s );
var l, str = "";

while( ( l = b.readLine() ) != null ) {
	// skip
	if( l != "" ) {
	str = str + l + "\n";
	}
}
// define the namespaces, first the default,
// then additional namespaces
default xml namespace = "http://purl.org/rss/1.0/";
var dc = new Namespace( "http://purl.org/dc/elements/1.1/" );
var rdf = new Namespace( "http://www.w3.org/1999/02/22-rdf-syntax-ns#" );

// use e4x to process the feed
var x = new XML( str );
for each( var i in x..item ) {
	print( "Title: " + i.title + "\n" );
	print( "About: " + i.@rdf::about + "\n" );
	print( "Link: " + i.link + "\n" );
	print( "Date: " + i.dc::date + "\n" );
}