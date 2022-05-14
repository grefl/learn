

function sort(a) {
  if (a.length < 2) return a; 
  const mid = parseInt(a.length / 2);
  const b = sort(a.slice(0, mid));
  const c = sort(a.slice(mid));
  return merge(b,c)
  
}

function merge(a,b) {
  
  const n = a.length
  const m = b.length
  const c = Array(n+m).fill(null);
  let i = 0;
  let j = 0;
  let k = 0;

  while (i < n || j < m) {
    if (j == m || (i < n && a[i] < b[j])) {
      c[k] = a[i];
      k+=1;
      i+=1;
    } else {
      c[k]= b[j];
      k+=1;
      j+=1;
    }
      
  }
  return c;
}


console.log(sort([23,4,56,3]))
