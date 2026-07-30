// class Solution {
//     public int hIndex(int[] citations) {
//         Arrays.sort(citations);
//         int h = 0;
//         while (h<citations.length && citations[h]<h+1){
//             // if (citations[h] == 0){
//             //     continue;
//             // }

//             h++;
            
//         }
//         return h;
//     }
// }

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n - i) {
                return n - i;
            }
        }
        
        return 0;
    }
}