import csv

# Fill in your flashcards here: [Front, Back]
flashcards = [flashcards_data = [
    {
        "front": "What major shift occurred in the 20th century regarding parenting?",
        "back": "Childbearing became a 'calculus of conscious choice' — a deliberate decision rather than being 'up to God or nature.'"
    },
    {
        "front": "How did effective birth control influence family size and ideology?",
        "back": "It made reduced childbearing socially acceptable and advantageous, especially as large families became economic burdens."
    },
    {
        "front": "What was the legal stance on birth control in Canada before destigmatization?",
        "back": "It was a criminal offense to sell, advertise, or possess contraceptives for preventing conception under the Canadian Criminal Code."
    },
    {
        "front": "What workaround existed for birth control in the 1960s?",
        "back": "Condoms could be used for disease prevention and the pill could be prescribed for menstrual regulation or cramps."
    },
    {
        "front": "Describe the pre-fertility transition period.",
        "back": "Parenthood was a core part of adulthood, began early, lacked contraception, and children were spaced unpredictably."
    },
    {
        "front": "Describe the post-fertility transition period.",
        "back": "Parenthood became a choice; fewer children, delayed births, separation from marriage, and competition with careers."
    },
    {
        "front": "What are the main contextual influences on childbearing?",
        "back": "Opportunity costs (education, income), sex education access, parental leave, childcare costs, and housing affordability."
    },
    {
        "front": "Why might young adults choose not to have children?",
        "back": "Financial pressure, unstable employment, housing costs, competing goals, and no desire for 'parent' as a master status."
    },
    {
        "front": "What is 'parenthood as master status'?",
        "back": "It defines one's primary identity and how they see or present themselves in society."
    },
    {
        "front": "What is 'baby shock'?",
        "back": "The unexpected emotional, financial, and relational challenges that follow the highly anticipated arrival of a child."
    },
    {
        "front": "How does parenthood typically affect income and marital satisfaction?",
        "back": "Income decreases, expenditures increase, and marital satisfaction often declines in early childhood years."
    },
    {
        "front": "What is 'intensive mothering' (Sharon Hays, 1996)?",
        "back": "A cultural norm where parenting is child-centered, expert-guided, labour-intensive, emotionally absorbing, and resource-heavy."
    },
    {
        "front": "What are the 'Couple Trajectories' in parenting roles?",
        "back": "Caregiver:Earner, Manager:Helper, Gatekeeper:Outsider, Equal:Equal, Alternate:Alternate — different work/role distributions."
    },
    {
        "front": "Describe Baumrind’s four parenting styles.",
        "back": "Authoritative (responsive), Authoritarian (strict), Permissive (lenient), and Uninvolved (neglectful)."
    },
    {
        "front": "How does Annette Lareau distinguish 'Natural Growth' vs 'Concerted Cultivation'?",
        "back": "'Natural Growth'—unstructured independence; 'Concerted Cultivation'—structured, achievement-focused, parental involvement."
    },
    {
        "front": "What is alloparenting?",
        "back": "Childrearing support shared beyond parents — by kin, friends, community, or professionals — challenging nuclear family norms."
    },
    {
        "front": "Who can be alloparents?",
        "back": "Recognized kin, fictive/voluntary kin, and professionals such as teachers or coaches."
    },
    {
        "front": "How did women’s paid work change in Canada post-1950s?",
        "back": "More married women and mothers joined the workforce, though wage and compensation gaps persisted."
    },
    {
        "front": "What factors widen the gender pay gap?",
        "back": "Hidden compensations, job sector differences, motherhood penalties, and men’s higher-paid private sector work."
    },
    {
        "front": "How does higher education impact the gender wage gap?",
        "back": "It reduces but does not eliminate it — gaps remain, especially among older workers and parents."
    },
    {
        "front": "What is the 'price of motherhood'?",
        "back": "Reduced lifetime earnings, higher part-time work, frequent workforce exits, and cumulative career setbacks."
    },
    {
        "front": "What is the feminization of poverty?",
        "back": "The trend of women—especially mothers and older women—being more likely to experience poverty due to unpaid care burdens."
    },
    {
        "front": "How has unpaid work in the home remained gendered?",
        "back": "Women still perform most unpaid work; men’s participation has increased slightly, especially in childcare."
    },
    {
        "front": "What is 'social reproduction' work?",
        "back": "Daily maintenance of life (cleaning, cooking, caregiving) that is repetitive, moralized, and largely unpaid."
    },
    {
        "front": "What is the 'triple shift' (Hochschild)?",
        "back": "Women perform paid work (first shift), domestic work (second shift), and emotional work (third shift)."
    },
    {
        "front": "What is the 'time bind'?",
        "back": "When work, caregiving, and personal demands exceed available time, leading to chronic stress and fatigue."
    },
    {
        "front": "How did COVID-19 affect unpaid work divisions?",
        "back": "Initially more equal, but later women faced greater interruptions and work-life strain, reinforcing old patterns."
    },
    {
        "front": "What is the 'commodification of domesticity'?",
        "back": "Outsourcing unpaid domestic work into the paid economy—e.g., childcare, eldercare, meal prep services."
    },
    {
        "front": "What distinguishes egalitarian vs neo-traditional arrangements?",
        "back": "Egalitarian couples share unpaid work equally; neo-traditional couples revert to gendered divisions after children."
    },
    {
        "front": "How do queer/same-sex couples typically differ in unpaid work patterns?",
        "back": "They divide work more equally and negotiate roles explicitly, without relying on heteronormative expectations."
    }
]
]

# Save flashcards as a CSV file
with open("flashcards.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(flashcards)

print("flashcards.csv has been created on your Desktop folder!")
