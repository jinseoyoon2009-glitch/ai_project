import streamlit as st

# MBTI별 음식과 디저트 추천 딕셔너리
mbti_recommendations = {
    'INTJ': {
        'food': ['초밥 🍣', '파스타 🍝'],
        'dessert': ['마카롱 🍬', '티라미수 🍰']
    },
    'INTP': {
        'food': ['샌드위치 🥪', '치킨너겟 🍗'],
        'dessert': ['치즈케이크 🍰', '브라우니 🍫']
    },
    'ENTJ': {
        'food': ['스테이크 🥩', '리조또 🍚'],
        'dessert': ['레몬 타르트 🍋', '크림 브륄레 🍮']
    },
    'ENTP': {
        'food': ['버거 🍔', '피자 🍕'],
        'dessert': ['도넛 🍩', '파블로바 🍓']
    },
    'INFJ': {
        'food': ['그릭 요거트 🍯', '채소 샐러드 🥗'],
        'dessert': ['베리 파르페 🍓', '소프트 아이스크림 🍦']
    },
    'INFP': {
        'food': ['라면 🍜', '떡볶이 🌶️'],
        'dessert': ['마들렌 🍪', '초콜릿 케이크 🍰']
    },
    'ENFJ': {
        'food': ['된장찌개 🍲', '김치찌개 🍛'],
        'dessert': ['한과 🍯', '호떡 🥞']
    },
    'ENFP': {
        'food': ['타코 🌮', '샐러드 🌱'],
        'dessert': ['케이크 🎂', '푸딩 🍮']
    },
    'ISTJ': {
        'food': ['돈까스 🍚', '갈비탕 🍖'],
        'dessert': ['식혜 🍹', '호두과자 🥮']
    },
    'ISFJ': {
        'food': ['김밥 🍱', '찌개 🍲'],
        'dessert': ['인절미 🍡', '식빵 🍞']
    },
    'ESTJ': {
        'food': ['삼겹살 🍖', '제육볶음 🍛'],
        'dessert': ['파운드케이크 🍰', '쿠키 🍪']
    },
    'ESFJ': {
        'food': ['떡볶이 🌶️', '볶음밥 🍳'],
        'dessert': ['케이크 🎂', '쿠키 🍪']
    },
    'ISTP': {
        'food': ['피자 🍕', '햄버거 🍔'],
        'dessert': ['아이스크림 🍦', '초콜릿 🍫']
    },
    'ISFP': {
        'food': ['스무디볼 🥣', '닭강정 🍗'],
        'dessert': ['파르페 🍨', '크레페 🥞']
    },
    'ESTP': {
        'food': ['타코 🌮', '핫도그 🌭'],
        'dessert': ['도넛 🍩', '케이크 🍰']
    },
    'ESFP': {
        'food': ['치킨 🍗', '떡볶이 🌶️'],
        'dessert': ['빙수 🍧', '컵케이크 🧁']
    }
}

# 스트림릿 UI 구성
st.title("MBTI 음식 & 디저트 추천 앱 🎉")

# MBTI 선택하기
mbti_type = st.selectbox(
    "당신의 MBTI를 선택해주세요! 😊",
    list(mbti_recommendations.keys())
)

# 선택된 MBTI에 맞는 음식과 디저트 추천
if mbti_type:
    st.subheader(f"{mbti_type}에게 추천하는 음식 & 디저트 🍽️🍰")
    
    # 음식 추천
    st.write("🍴 **추천 음식**:")
    for food in mbti_recommendations[mbti_type]['food']:
        st.write(food)
    
    # 디저트 추천
    st.write("🍨 **추천 디저트**:")
    for dessert in mbti_recommendations[mbti_type]['dessert']:
        st.write(dessert)

# 기본적인 디자인과 UX를 고려해서 좀 더 직관적인 선택을 제공
st.markdown("---")
st.markdown("MBTI에 맞는 음식을 추천해줄게! 너만의 스타일을 찾아봐 👀")
