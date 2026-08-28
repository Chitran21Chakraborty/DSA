class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for opr in operations:
            if opr == '++X' or opr=='X++':
                X+=1
            else:
                X-=1
        return X