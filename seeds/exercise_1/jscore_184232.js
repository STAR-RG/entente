// Anny
// https://bugs.webkit.org/show_bug.cgi?id=184232
const buffer = new ArrayBuffer(8)
const view = new Uint8Array(buffer, undefined, undefined)

if (!(view.length === 8)) {
    throw new Error("Test failed");
}
