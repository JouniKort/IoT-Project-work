A = [0,0,0,0,0]

function medianFilter(velocity){
  for(i = 0; i < A.length - 1; i++){
    A[i] = A[i+1]
  }
  A[A.length-1] = velocity
  return median(A.slice())
}

median = (A) => A.sort()[Math.floor(A.length/2)]

module.exports.medianFilter = medianFilter