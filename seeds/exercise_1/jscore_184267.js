//https://bugs.webkit.org/show_bug.cgi?id=184267

const proxy = new Proxy([3, 4], {});
const res = [1, 2].concat(proxy);

if((res[3]===undefined)){
    throw new Error('Test failed');
}