import java.util.Arrays;

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = 0;
        
        // Count how many papers from the end of the sorted array have at least h + 1 citations
        while (h < n && citations[n - 1 - h] > h) {
            h++;
        }
        
        return h;
    }
}

// class Solution {
//     public int hIndex(int[] citations) {
//         Arrays.sort(citations);
//         int n = citations.length;
        
//         for (int i = 0; i < n; i++) {
//             if (citations[i] >= n - i) {
//                 return n - i;
//             }
//         }
        
//         return 0;
//     }
// }