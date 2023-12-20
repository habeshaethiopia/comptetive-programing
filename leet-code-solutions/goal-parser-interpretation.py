class Solution:
    def interpret(self, command: str) -> str:
        st=""
        if command[0] not in ["(", ")"]:
            st += command[0]
        for i in range(1,len(command)):
            if command[i-1]=="(" and command[i]==")":
                st += "o"
            else:
                if(command[i-1]=="(" ) and command[i]!=")":
                    st += command[i]
                elif command[i] not in ["(", ")"]:
                    st += command[i]
        print(st)
        return (st)
