export function serialize(data: Record<string, any>) {
  var str = [];
  for (var p in data)
    if (data.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(data[p]));
    }
  return str.join("&");
}
