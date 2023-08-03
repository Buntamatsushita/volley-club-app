import random
import streamlit as st


def main():
    st.title("メンバー抽選")
    
    st.write("メンバーを抽選します。")
    
    
    mode = st.selectbox("抽選モード", ("名前有チーム分け", "ルーレット"))
    
    team_num = st.number_input("チーム数", 1, 5, 1)
    
    
    if mode == "名前有チーム分け":
        member_list = {}
        result = []
        
        member_name = st.text_area("メンバー名", "名前を入力してください")
        if st.button("メンバー追加"):
            if member_name[0] != "名前を入力してください":
                st.error("メンバー名を入力してください")
            else:
                for i in member_name.split("\n"):
                    member_list[i] = random.randint(1,20000)
                member_list = sorted(member_list.items(), key=lambda x:x[1])
                
                tmp_times = 0
                for i in range(team_num):
                    result.append([])
                
                for i in member_list:
                    result[tmp_times].append(i[0])
                    tmp_times += 1
                    if tmp_times == team_num:
                        tmp_times = 0
                    

        if result != []:
            for i in range(team_num):
                st.subheader("チーム{}".format(i+1))
                for j in result[i]:
                    st.write(j)
                st.write(" ")
            
        
    elif mode == "ルーレット":
        menber_num = st.slider("メンバー数", 1, 20, 1)
        menber_num_list = []
        if st.button("抽選"):
            chosen = random.randint(1, team_num)
            while menber_num_list[chosen-1] < (menber_num/team_num):
                chosen = random.randint(1, team_num)
                menber_num_list[chosen-1] += 1
            st.write("チーム{}".format(chosen))

    
if __name__ == "__main__":
    main()