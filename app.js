/* ==========================================
   APPLYWISE AI - CORE APPLICATION SCRIPT
   ========================================== */

// --- PRE-LOADED BILINGUAL TECH TEMPLATES ---
const JOB_TEMPLATES = {
  shopify: {
    company: "Shopify",
    role: "Bilingual Full-Stack Developer",
    location: "Ottawa, ON (Hybrid / Remote)",
    tags: ["React", "Ruby on Rails", "Bilingual Asset"],
    jd: `About the Role:
Shopify is looking for a Bilingual Full-Stack Developer to join our core merchant experience team. You will work on building scalable web applications that power millions of merchants globally. This role is based out of our Ottawa headquarters with flexible hybrid and remote options.

Key Responsibilities:
- Design and develop highly interactive web frontends using React, TypeScript, and modern state management.
- Build robust, scalable backend APIs using Ruby on Rails and PostgreSQL.
- Collaborate with product managers, designers, and other engineering teams.
- Support our bilingual merchant base (English and French). While technical documentation is in English, the ability to communicate with merchants and write user-facing content in both French and English is a strong asset.

Requirements:
- 3+ years of experience in full-stack web development.
- Strong proficiency in React/JavaScript and Ruby on Rails or a similar backend framework.
- Experience with RESTful APIs, GraphQL, and relational databases.
- Strong communication skills in English and French (bilingual proficiency).`,
    resume: `Jean-Pierre Tremblay
Ottawa, ON | jp.tremblay@email.com | (613) 555-0199

Summary:
Full-Stack Developer with 4 years of experience building web applications. Highly proficient in React, JavaScript, and Node.js. Intermediate communication skills in French, seeking to transition into a bilingual technical role.

Experience:
Web Developer | TechNorth Solutions, Toronto (Remote) | 2022 - Present
- Built and maintained client-facing dashboards using React and Redux, improving load times by 20%.
- Developed backend microservices using Node.js, Express, and MongoDB.
- Participated in Agile sprint planning and daily standups.

Junior Developer | DevStudio, Montreal, QC | 2020 - 2022
- Developed UI components using HTML, CSS, and Vue.js.
- Assisted in writing database migrations and API endpoints in Python/Django.
- Wrote unit tests in Jest, increasing coverage by 15%.

Education & Skills:
- B.Sc. in Computer Science | Carleton University, Ottawa
- Languages: English (Fluent), French (Intermediate/B2)
- Tech: React, Node.js, Express, Vue.js, PostgreSQL, MongoDB, Git, Agile`,
    analysis: {
      score: 78,
      techScore: 70,
      langScore: 85,
      expScore: 80,
      verdict: "Strong Match with Minor Skill Gaps",
      techSkills: [
        { name: "React & Modern JS", match: true },
        { name: "Ruby on Rails", match: false, note: "Strong in Node.js/Python, needs Rails ramp-up." },
        { name: "PostgreSQL & Databases", match: true },
        { name: "GraphQL & APIs", match: true }
      ],
      langSkills: [
        { name: "English (Professional)", match: true },
        { name: "French (Bilingual communication)", match: false, note: "Intermediate (B2) - needs tech vocabulary coaching." }
      ],
      gaps: [
        { title: "Backend Stack (Ruby on Rails)", action: "Study basic Rails MVC, ActiveRecord, and routing patterns." },
        { title: "Professional French Vocabulary", action: "Review French terms for Agile sprints, Git workflows, and UI components." }
      ],
      academy: [
        { title: "Ruby on Rails for React Developers", desc: "A fast-track course covering Rails API development for developers with existing frontend experience.", provider: "Pragmatic Studio" },
        { title: "Le Français dans les TI (IT French)", desc: "A specialized language course focused on French terminology in software engineering and Agile teams.", provider: "Alliance Française Ottawa" }
      ],
      bullets: {
        en: [
          { original: "Built and maintained client-facing dashboards using React and Redux, improving load times by 20%.", tailored: "Architected bilingual merchant dashboards in React and Redux, optimizing load times by 20% to support high-traffic global storefronts." },
          { original: "Developed backend microservices using Node.js, Express, and MongoDB.", tailored: "Developed scalable REST/GraphQL APIs (transitioning to Ruby on Rails principles) and integrated PostgreSQL databases." },
          { original: "Participated in Agile sprint planning and daily standups.", tailored: "Collaborated in bilingual Agile environments, participating in daily standups and sprint planning in both English and French." }
        ],
        fr: [
          { original: "Built and maintained client-facing dashboards using React and Redux...", tailored: "Conçu et optimisé des tableaux de bord bilingues avec React et Redux, réduisant les temps de chargement de 20 % pour nos marchands." },
          { original: "Developed backend microservices using Node.js...", tailored: "Développé des microservices et API robustes, avec une transition active vers l'écosystème Ruby on Rails et PostgreSQL." },
          { original: "Participated in Agile sprint planning...", tailored: "Collaboré activement au sein d'équipes Agile bilingues, participant aux mêlées quotidiennes et planifications en anglais et en français." }
        ]
      },
      pitches: {
        bilingual: "Hi, I'm Jean-Pierre. I'm a Full-Stack Developer with 4 years of experience specializing in React and Node.js. Ayant grandi à Ottawa, je suis parfaitement à l'aise dans un environnement bilingue. I've built highly scalable merchant dashboards, and I'm excited to bring my React expertise to Shopify. Je suis également impatient de monter en compétences sur Ruby on Rails pour soutenir pleinement vos équipes techniques dans les deux langues.",
        en: "Hi, I'm Jean-Pierre. I'm a Full-Stack Developer with 4 years of experience, specializing in React and modern JavaScript. I have a proven track record of optimizing merchant-facing dashboards and building scalable APIs. Being based in Ottawa, I am highly comfortable working in a bilingual environment, allowing me to collaborate effectively with both English and French-speaking teams and merchants.",
        fr: "Bonjour, je m'appelle Jean-Pierre. Je suis développeur Full-Stack avec 4 ans d'expérience, spécialisé en React et Node.js. Résidant à Ottawa, je travaille couramment en anglais et en français. J'ai conçu des tableaux de bord performants et je souhaite apporter cette expertise à Shopify, tout en développant mes compétences sur Ruby on Rails pour répondre aux besoins de vos marchands bilingues."
      },
      coverLetters: {
        hybrid: `Jean-Pierre Tremblay
Ottawa, ON | jp.tremblay@email.com
June 30, 2026

À l'attention de l'équipe de recrutement
Shopify
Ottawa, ON

Objet : Candidature pour le poste de Développeur Full-Stack Bilingue

Madame, Monsieur,

C'est avec un grand enthousiasme que je soumets ma candidature pour le poste de Développeur Full-Stack Bilingue chez Shopify. En tant que développeur basé à Ottawa et utilisateur de longue date de la plateforme Shopify, je suis impressionné par votre engagement à soutenir les marchands du monde entier. Je souhaite mettre à profit mon expertise en développement web moderne pour contribuer à cette mission, tout en assurant une collaboration bilingue fluide.

During my four years of professional experience, I have specialized in building highly responsive frontends using React and Redux, as well as robust backend services. At TechNorth Solutions, I led the redesign of our merchant analytics dashboard, which successfully reduced page load times by 20% and directly improved customer retention. While my primary backend experience is in Node.js, I have already begun training in Ruby on Rails and PostgreSQL, and I am eager to apply my strong database foundation to Shopify's codebase.

De plus, mon bilinguisme me permet d'évoluer aisément dans des équipes de développement mixtes. Qu'il s'agisse de rédiger de la documentation technique en anglais ou de collaborer avec des partenaires francophones lors des réunions de planification Agile, je m'assure toujours que la communication reste claire et efficace.

Je serais ravi de vous rencontrer lors d'un entretien pour discuter de la manière dont mes compétences techniques et linguistiques peuvent aider Shopify à propulser le commerce local et international.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Jean-Pierre Tremblay`,
        en: `Jean-Pierre Tremblay
Ottawa, ON | jp.tremblay@email.com
June 30, 2026

Hiring Team
Shopify
Ottawa, ON

Subject: Application for Bilingual Full-Stack Developer Role

Dear Shopify Hiring Team,

I am writing to express my strong interest in the Bilingual Full-Stack Developer position at Shopify. With four years of hands-on experience building scalable web applications, a deep specialization in React, and professional bilingual proficiency in English and French, I am excited about the opportunity to contribute to Shopify's merchant-facing engineering teams.

In my previous role at TechNorth Solutions, I focused on developing high-performance user interfaces using React and Redux, successfully optimizing client-facing dashboards to improve load times by 20%. On the backend, I designed and maintained microservices using Node.js and SQL databases. Although my primary backend experience is in Node.js, I am highly adaptable and have already begun building local projects with Ruby on Rails to ensure a rapid onboarding process into Shopify's ecosystem.

Working in Canada's tech corridor has shown me the immense value of bilingual collaboration. I am fully equipped to write clean technical documentation in English while engaging in daily standups, code reviews, and merchant communications in both French and English. 

Thank you for your time and consideration. I look forward to discussing how my technical background and bilingual capabilities align with Shopify's goals.

Sincerely,

Jean-Pierre Tremblay`,
        fr: `Jean-Pierre Tremblay
Ottawa, ON | jp.tremblay@email.com
June 30, 2026

Équipe de recrutement
Shopify
Ottawa, ON

Objet : Candidature pour le poste de Développeur Full-Stack Bilingue

Madame, Monsieur,

Je vous adresse ma candidature pour le poste de Développeur Full-Stack Bilingue chez Shopify. Fort de quatre années d'expérience dans la création d'applications web performantes, spécialisé en React et résidant à Ottawa, je suis enthousiaste à l'idée de rejoindre une entreprise canadienne emblématique qui transforme le commerce mondial.

Lors de mon parcours chez TechNorth Solutions, j'ai conçu des tableaux de bord interactifs en React et Redux, ce qui a permis d'optimiser le temps de chargement de 20 % et d'améliorer l'expérience utilisateur globale. Sur le plan dorsal, j'ai développé des microservices avec Node.js et géré des bases de données relationnelles. Je possède une solide compréhension des architectures MVC et je maîtrise déjà les concepts clés de Ruby on Rails, ce qui me permettra d'être rapidement opérationnel au sein de votre équipe technique.

Mon bilinguisme est un atout majeur pour ce poste. Je suis habitué à naviguer entre l'anglais et le français, que ce soit pour rédiger du code et de la documentation technique ou pour animer des ateliers et communiquer avec vos marchands francophones.

Je vous remercie de l'attention que vous porterez à ma candidature et reste à votre entière disposition pour un entretien.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Jean-Pierre Tremblay`
      },
      interview: [
        { q: "Tell me about yourself and your experience with React. / Parlez-moi de vous et de votre expérience avec React.", lang: "bilingual" },
        { q: "Shopify uses Ruby on Rails extensively. How do you plan to transition to Rails from Node.js?", lang: "en" },
        { q: "Pouvez-vous me parler d'une situation où vous avez dû travailler en équipe dans un contexte bilingue ?", lang: "fr" },
        { q: "Explain the difference between SQL and NoSQL databases, and when you would use each.", lang: "en" },
        { q: "Comment gérez-vous le stress ou les priorités conflictuelles lors d'un sprint Agile ?", lang: "fr" }
      ],
      checklist: [
        "Tailor resume bullets to highlight React dashboard optimization",
        "Add Ruby on Rails basic course to LinkedIn certifications",
        "Draft the Bilingual Hybrid cover letter proving written French capabilities",
        "Practice the 30-second bilingual elevator pitch",
        "Review French terms for Agile sprints (mêlée quotidienne, carnet de produit)",
        "Confirm Ottawa office hybrid work schedule requirements"
      ]
    }
  },
  coveo: {
    company: "Coveo",
    role: "Senior DevOps & Cloud Engineer",
    location: "Montreal, QC (Hybrid)",
    tags: ["AWS", "Kubernetes", "French Imperative"],
    jd: `About Coveo:
Coveo is a pioneer in AI-powered search and recommendation engines. We are looking for a Senior DevOps & Cloud Engineer to join our infrastructure team in Montreal. This role requires a strong focus on automation, containerization, and cloud security.

Key Responsibilities:
- Manage, scale, and optimize our global AWS cloud infrastructure.
- Orchestrate containerized microservices using Kubernetes (EKS).
- Build and maintain robust CI/CD pipelines (GitLab CI, Terraform).
- Collaborate with development teams to ensure high availability and security.
- French Language Requirement: In accordance with Quebec's Bill 96, team collaboration, technical meetings, and internal communications in our Montreal office are primarily conducted in French. Professional French proficiency is imperative.

Requirements:
- 5+ years of DevOps/Cloud engineering experience.
- Strong expertise with AWS, Terraform, and Kubernetes.
- Experience with Docker, CI/CD tools, and scripting (Python/Bash).
- Professional level fluency in French (written and spoken) is required.`,
    resume: `Sarah Jenkins
Montreal, QC | sarah.jenkins@email.com | (514) 555-0144

Summary:
Senior DevOps Engineer with 6 years of experience specializing in cloud infrastructure automation, Kubernetes orchestration, and CI/CD pipelines. Native English speaker with working proficiency in French, actively improving technical French communication.

Experience:
Cloud Infrastructure Engineer | CloudScale Inc., Vancouver (Remote) | 2021 - Present
- Automated AWS infrastructure provisioning using Terraform, reducing deployment times by 40%.
- Managed production Kubernetes clusters (EKS) hosting 50+ microservices.
- Implemented Prometheus and Grafana monitoring, reducing incident resolution time by 30%.

DevOps Engineer | StartupHub, Montreal, QC | 2019 - 2021
- Built CI/CD pipelines using GitHub Actions and Docker.
- Managed Google Cloud Platform (GCP) resources and SQL databases.
- Scripted automation tasks in Python and Bash, saving 10 engineering hours weekly.

Education & Skills:
- B.Eng. in Software Engineering | McGill University, Montreal
- AWS Certified Solutions Architect - Professional
- Certified Kubernetes Administrator (CKA)
- Languages: English (Native), French (B1/Intermediate - Professional Speaking in Progress)
- Tech: AWS, GCP, Kubernetes, Terraform, Docker, Python, Bash, CI/CD, Git`,
    analysis: {
      score: 82,
      techScore: 95,
      langScore: 65,
      expScore: 85,
      verdict: "Excellent Technical Fit, French Language Gap",
      techSkills: [
        { name: "AWS Cloud (AWS Certified Pro)", match: true },
        { name: "Kubernetes (CKA)", match: true },
        { name: "Terraform & IaC", match: true },
        { name: "CI/CD Pipelines", match: true }
      ],
      langSkills: [
        { name: "French (Team Collaboration)", match: false, note: "B1 level. Needs support for technical discussions in French." },
        { name: "English (Technical)", match: true }
      ],
      gaps: [
        { title: "Quebec Workplace French (Bill 96)", action: "Practice describing infrastructure, deployment pipelines, and incident resolution in French." },
        { title: "French Technical Jargon", action: "Learn French terms for cloud concepts (e.g., 'hébergement en nuage', 'conteneurisation', 'pipeline de déploiement')." }
      ],
      academy: [
        { title: "French for Tech Professionals", desc: "Specialized language coaching for engineers working in Quebec tech hubs. Focuses on standup vocabulary and technical presentations.", provider: "OQLF / Government of Quebec Language Programs" },
        { title: "Le Vocabulaire DevOps en Français", desc: "A curated guide to managing server configurations and deployments in French-speaking teams.", provider: "ApplyWise Academy" }
      ],
      bullets: {
        en: [
          { original: "Automated AWS infrastructure provisioning using Terraform, reducing deployment times by 40%.", tailored: "Automated multi-region AWS cloud infrastructure using Terraform, reducing provisioning times by 40% in compliance with high-availability standards." },
          { original: "Managed production Kubernetes clusters (EKS) hosting 50+ microservices.", tailored: "Orchestrated production Kubernetes (EKS) clusters hosting 50+ critical microservices, achieving 99.99% uptime." },
          { original: "Scripted automation tasks in Python and Bash, saving 10 engineering hours weekly.", tailored: "Created Python and Bash automation scripts for infrastructure scaling, reducing manual overhead by 10 hours weekly." }
        ],
        fr: [
          { original: "Automated AWS infrastructure provisioning using Terraform...", tailored: "Automatisé le provisionnement de l'infrastructure AWS multi-régions à l'aide de Terraform, réduisant les délais de déploiement de 40 %." },
          { original: "Managed production Kubernetes clusters (EKS)...", tailored: "Géré et orchestré des clusters Kubernetes (EKS) en production hébergeant plus de 50 microservices, garantissant une disponibilité de 99,99 %." },
          { original: "Scripted automation tasks in Python and Bash...", tailored: "Développé des scripts d'automatisation en Python et Bash pour la mise à l'échelle de l'infrastructure, économisant 10 heures d'ingénierie par semaine." }
        ]
      },
      pitches: {
        bilingual: "Hi, I'm Sarah. I'm a Senior DevOps Engineer with 6 years of experience specializing in AWS and Kubernetes. Côté technique, je suis certifiée CKA et AWS Professional. J'ai automatisé des infrastructures complexes avec Terraform. I'm excited about Coveo's AI mission. Bien que ma langue maternelle soit l'anglais, je travaille activement mon français professionnel pour m'intégrer parfaitement à votre équipe de Montréal.",
        en: "Hi, I'm Sarah. I'm a Senior DevOps Engineer with 6 years of experience, holding CKA and AWS Certified Solutions Architect Professional credentials. I specialize in scaling Kubernetes clusters and automating infrastructure with Terraform. Having lived in Montreal, I am excited about joining Coveo and am fully committed to conducting team collaborations and technical standups in French.",
        fr: "Bonjour, je m'appelle Sarah. Je suis ingénieure DevOps Senior avec 6 ans d'expérience. Je suis certifiée AWS Professional et CKA (Kubernetes). J'ai géré des clusters d'envergure et automatisé des déploiements avec Terraform. Je suis très motivée à rejoindre Coveo à Montréal et à animer nos réunions et collaborations quotidiennes en français."
      },
      coverLetters: {
        hybrid: `Sarah Jenkins
Montréal, QC | sarah.jenkins@email.com
June 30, 2026

À l'attention de l'équipe de recrutement
Coveo
Montréal, QC

Objet : Candidature pour le poste d'Ingénieure DevOps Senior

Madame, Monsieur,

C'est avec un grand intérêt que je pose ma candidature pour le poste d'Ingénieure DevOps Senior au sein de l'équipe d'infrastructure de Coveo à Montréal. Ayant suivi de près l'évolution de Coveo comme leader de la recherche IA, je souhaite apporter mon expertise en orchestration de conteneurs et en automatisation de l'infrastructure pour soutenir votre croissance technologique.

Over the past six years, I have engineered reliable cloud platforms. In my current role at CloudScale Inc., I designed and managed our production Kubernetes (EKS) infrastructure, deploying over 50 microservices and implementing Prometheus/Grafana monitoring that reduced incident resolution times by 30%. Additionally, I automated our entire AWS infrastructure provisioning using Terraform, which cut deployment times by 40% and eliminated configuration drift.

Habitant à Montréal, je comprends l'importance de la langue française dans le milieu de travail québécois. Bien que ma langue maternelle soit l'anglais, je possède un niveau intermédiaire solide en français (B1) et je m'exprime quotidiennement dans cette langue. Je m'engage pleinement à mener mes interactions professionnelles, réunions techniques et mêlées quotidiennes en français chez Coveo, tout en m'appuyant sur mon bagage technique anglophone pour la documentation système globale.

Je vous remercie de l'intérêt porté à ma candidature et je serais ravie de vous exposer de vive voix comment je peux contribuer à optimiser la fiabilité des systèmes de Coveo.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Sarah Jenkins`,
        en: `Sarah Jenkins
Montréal, QC | sarah.jenkins@email.com
June 30, 2026

Hiring Team
Coveo
Montréal, QC

Subject: Application for Senior DevOps & Cloud Engineer Role

Dear Coveo Hiring Team,

I am writing to express my interest in the Senior DevOps & Cloud Engineer position at Coveo. As a certified Kubernetes Administrator (CKA) and AWS Solutions Architect Professional with six years of experience building secure, scalable cloud infrastructure, I am eager to bring my automation expertise to your Montreal-based team.

At CloudScale Inc., I managed large-scale production Kubernetes (EKS) clusters hosting dozens of microservices. I established a GitOps continuous deployment workflow using Terraform and GitLab CI, reducing provisioning times by 40%. I also designed comprehensive observability pipelines that decreased production recovery times. I thrive in complex environments where reliability and performance are paramount.

As a Montreal resident, I am highly comfortable working in a bilingual setting. I possess intermediate French capabilities and am fully prepared to conduct my day-to-day team collaborations, standups, and internal communications in French, ensuring seamless alignment with local team members and Quebec workplace regulations.

Thank you for your consideration. I look forward to discussing how my technical skills and local bilingual commitment can support Coveo's infrastructure.

Sincerely,

Sarah Jenkins`,
        fr: `Sarah Jenkins
Montréal, QC | sarah.jenkins@email.com
June 30, 2026

Équipe de recrutement
Coveo
Montréal, QC

Objet : Candidature pour le poste d'Ingénieure DevOps Senior

Madame, Monsieur,

Je soumets ma candidature pour le poste d'Ingénieure DevOps Senior chez Coveo. Forte d'une expérience de six ans en automatisation de l'infrastructure infonuagique et en orchestration Kubernetes, je souhaite rejoindre vos équipes de Montréal pour participer à l'optimisation de vos plateformes de recherche IA.

Chez CloudScale Inc., j'ai administré des clusters Kubernetes (EKS) en production accueillant plus de 50 microservices, maintenant un taux de disponibilité de 99,99 %. Grâce à Terraform, j'ai automatisé le provisionnement de nos environnements AWS, ce qui a permis de réduire les délais de déploiement de 40 %. De plus, j'ai mis en place des solutions de surveillance avec Prometheus et Grafana qui ont accéléré la résolution des incidents de 30 %.

Ma maîtrise intermédiaire du français me permet de m'intégrer sans difficulté dans l'environnement de travail de Coveo à Montréal. Je suis tout à fait disposée à mener les réunions d'équipe, les discussions techniques et les planifications en français, contribuant ainsi à la vie professionnelle de l'entreprise dans sa langue officielle.

Je vous remercie de l'attention accordée à ma candidature et reste disponible pour vous rencontrer.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Sarah Jenkins`
      },
      interview: [
        { q: "Pouvez-vous décrire votre expérience avec l'orchestration de conteneurs sous Kubernetes ?", lang: "fr" },
        { q: "How do you manage secrets and sensitive variables in your Terraform configurations?", lang: "en" },
        { q: "Comment expliquez-vous le concept d'Infrastructure as Code à un membre de l'équipe non technique, en français ?", lang: "fr" },
        { q: "Describe a time when you had to troubleshoot a critical production outage. What was your process?", lang: "en" },
        { q: "Comment gérez-vous la transition vers un environnement de travail dont la langue officielle est le français ?", lang: "fr" }
      ],
      checklist: [
        "Translate Terraform and AWS technical achievements to French for the Montreal team",
        "Obtain French translation of CKA and AWS certifications descriptions",
        "Prepare French explanations for common Kubernetes disaster recovery scenarios",
        "Review Quebec Bill 96 compliance details for Montreal tech workplaces",
        "Draft the Bilingual Hybrid cover letter proving commitment to French-first collaboration",
        "Schedule a mock technical interview in French"
      ]
    }
  },
  rbc: {
    company: "RBC",
    role: "Bilingual Technical Product Manager",
    location: "Toronto / Montreal (Hybrid)",
    tags: ["Agile", "Roadmapping", "Bilingual Client-Facing"],
    jd: `About the Role:
RBC is seeking a Bilingual Technical Product Manager to lead the development of our next-generation digital banking APIs. You will act as the bridge between software engineering teams, business stakeholders, and enterprise clients across Canada.

Key Responsibilities:
- Define and drive the product roadmap for RBC's developer platform APIs.
- Translate complex business needs into technical requirements, user stories, and acceptance criteria.
- Lead Agile ceremonies (sprint planning, backlog grooming, retrospectives).
- Engage with enterprise clients and partners in both English and French. Strong written and verbal communication skills in both official languages are required.

Requirements:
- 4+ years of Product Management or Technical Product Owner experience in fintech or enterprise software.
- Deep understanding of API design, microservices, and modern software architecture.
- Certified Scrum Product Owner (CSPO) or similar Agile certification.
- Fluent bilingualism (English and French) is mandatory for client presentations.`,
    resume: `Marc-André Roy
Montreal, QC | ma.roy@email.com | (514) 555-0122

Summary:
Technical Product Owner with 5 years of experience leading cross-functional Agile teams in the fintech space. Expert in API integrations, backlog management, and stakeholder communications. Fully bilingual in French and English.

Experience:
Product Owner | FinPay Technologies, Montreal, QC | 2021 - Present
- Managed the API integration product backlog, increasing developer onboarding efficiency by 35%.
- Defined user stories and technical requirements for payment processing microservices.
- Led Agile scrum teams of 8 developers, facilitating all sprint ceremonies in both English and French.

Technical Analyst | Quebec Capital, Quebec City, QC | 2019 - 2021
- Gathered and documented technical requirements for legacy system migrations.
- Conducted API testing using Postman and drafted developer documentation.
- Delivered biweekly progress demonstrations to corporate stakeholders.

Education & Skills:
- B.B.A. in Business Technology Management | HEC Montréal
- Certified Scrum Product Owner (CSPO)
- Languages: French (Native), English (Fluent / Bilingual)
- Tech: Jira, Confluence, Postman, SQL, REST APIs, Agile, Scrum, Figma`,
    analysis: {
      score: 94,
      techScore: 90,
      langScore: 98,
      expScore: 95,
      verdict: "Outstanding Match (Bilingual Champion)",
      techSkills: [
        { name: "API Design & REST", match: true },
        { name: "Agile & Scrum (CSPO)", match: true },
        { name: "Fintech Experience", match: true },
        { name: "Technical Requirements", match: true }
      ],
      langSkills: [
        { name: "French (Native/Client-Facing)", match: true },
        { name: "English (Fluent/Client-Facing)", match: true }
      ],
      gaps: [
        { title: "Enterprise Scaling (SAFe)", action: "RBC uses Scaled Agile Framework (SAFe). Review SAFe product manager patterns." }
      ],
      academy: [
        { title: "SAFe Product Owner/Product Manager (POPM)", desc: "Learn how to scale Agile practices across large enterprise financial organizations.", provider: "Scaled Agile Academy" },
        { title: "Bilingual Fintech Leadership", desc: "Mastering executive-level presentations in English and French within the Canadian banking sector.", provider: "ApplyWise Executive Coaching" }
      ],
      bullets: {
        en: [
          { original: "Managed the API integration product backlog, increasing developer onboarding efficiency by 35%.", tailored: "Managed the enterprise API developer platform backlog, streamlining partner onboarding by 35% across Canadian fintech integrations." },
          { original: "Led Agile scrum teams of 8 developers, facilitating all sprint ceremonies in both English and French.", tailored: "Led cross-functional Agile Scrum teams (8 developers), facilitating bilingual standups, backlog grooming, and sprint planning in English and French." },
          { original: "Conducted API testing using Postman and drafted developer documentation.", tailored: "Conducted API validation and compiled bilingual developer portal documentation, reducing onboarding friction." }
        ],
        fr: [
          { original: "Managed the API integration product backlog...", tailored: "Géré le carnet de produit des API d'entreprise, améliorant l'efficacité de l'intégration des développeurs de 35 % pour les partenaires canadiens." },
          { original: "Led Agile scrum teams of 8 developers...", tailored: "Dirigé des équipes Agile Scrum de 8 développeurs, animant toutes les cérémonies (planification, revues) en français et en anglais." },
          { original: "Conducted API testing using Postman...", tailored: "Effectué des tests d'API et rédigé la documentation technique bilingue du portail des développeurs." }
        ]
      },
      pitches: {
        bilingual: "Bonjour, je m'appelle Marc-André. I'm a Technical Product Owner with 5 years of experience in fintech, specializing in API platforms and Agile leadership. Je suis parfaitement bilingue, ayant dirigé des équipes techniques et présenté des feuilles de route produit à des clients d'affaires en français et en anglais. I'm excited about the opportunity to scale RBC's digital banking APIs across Canada.",
        en: "Hi, I'm Marc-André. I'm a Technical Product Owner with 5 years of experience in fintech. I specialize in managing developer platforms and API integrations. I have a strong technical background and hold a CSPO certification. I am fully bilingual and have extensive experience presenting product roadmaps and aligning technical teams with enterprise business stakeholders in both English and French.",
        fr: "Bonjour, je m'appelle Marc-André. Je suis Product Owner technique avec 5 ans d'expérience dans la fintech, spécialisé dans les plateformes API et les architectures de microservices. Certifié CSPO, je suis parfaitement bilingue. J'ai l'habitude d'animer des équipes de développeurs et de présenter des feuilles de route produit à des clients corporatifs en français et en anglais."
      },
      coverLetters: {
        hybrid: `Marc-André Roy
Montréal, QC | ma.roy@email.com
June 30, 2026

À l'attention du comité de recrutement
RBC (Banque Royale du Canada)
Montréal / Toronto

Objet : Candidature pour le poste de Product Manager Technique Bilingue

Madame, Monsieur,

C'est avec un vif intérêt que je soumets ma candidature pour le poste de Product Manager Technique Bilingue pour votre plateforme d'API bancaires numériques. Fort de mon expérience de cinq ans en gestion de produits fintech et de mon bilinguisme parfait, je suis convaincu de pouvoir guider vos équipes d'ingénierie tout en assurant une relation de confiance avec vos partenaires à travers le Canada.

In my current role at FinPay Technologies, I have owned the API integration roadmap, collaborating with engineering leads to design secure, scalable payment microservices. By restructuring our developer portal and documentation, I successfully reduced partner onboarding times by 35%. I am highly comfortable translating complex business objectives into detailed user stories, technical specifications, and clear acceptance criteria for development teams.

Ayant évolué dans le secteur financier à Montréal et Québec, le travail en contexte bilingue fait partie de mon quotidien. J'anime régulièrement des mêlées quotidiennes et des sessions de cadrage en français et en anglais. De plus, j'ai l'habitude de présenter des feuilles de route produit complexes et des rapports d'avancement à des cadres supérieurs et des clients corporatifs dans les deux langues.

Je serais ravi de vous rencontrer lors d'un entretien afin de discuter de ma contribution future au développement des solutions numériques de la RBC.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Marc-André Roy`,
        en: `Marc-André Roy
Montréal, QC | ma.roy@email.com
June 30, 2026

Hiring Committee
RBC (Royal Bank of Canada)
Toronto / Montreal

Subject: Application for Bilingual Technical Product Manager Role

Dear RBC Hiring Committee,

I am writing to express my strong interest in the Bilingual Technical Product Manager position at RBC. With five years of experience leading cross-functional Agile teams in the fintech sector, a solid background in API design, and complete bilingual fluency in English and French, I am eager to help drive the roadmap for RBC's developer platform.

In my current role as a Technical Product Owner at FinPay Technologies, I manage the product backlog for our core payment APIs. I work closely with engineering teams to design RESTful microservices while collaborating with business stakeholders to align deliverables. By prioritizing developer experience and streamlining API documentation, I improved partner onboarding efficiency by 35%.

As a fully bilingual professional, I have successfully facilitated Agile ceremonies and delivered executive-level presentations in both official languages. I am well-prepared to collaborate with engineering teams in Toronto and Montreal, as well as present RBC's digital banking capabilities to enterprise clients across Canada.

Thank you for your time and consideration. I look forward to the opportunity to discuss how my fintech background and bilingual leadership can benefit RBC.

Sincerely,

Marc-André Roy`,
        fr: `Marc-André Roy
Montréal, QC | ma.roy@email.com
June 30, 2026

Comité de recrutement
RBC (Banque Royale du Canada)
Montréal / Toronto

Objet : Candidature pour le poste de Product Manager Technique Bilingue

Madame, Monsieur,

Je vous propose ma candidature pour le poste de Product Manager Technique Bilingue chez RBC. Passionné par l'innovation financière et fort de cinq années d'expérience en gestion de produits d'API dans la fintech, je souhaite contribuer au succès de vos plateformes de services bancaires numériques.

Au cours de mon mandat chez FinPay Technologies, j'ai géré le carnet de produit pour nos API de paiement, collaborant étroitement avec les architectes logiciels pour définir les spécifications des microservices. Mes efforts d'optimisation de la documentation technique ont permis d'accélérer l'intégration des développeurs partenaires de 35 %. Certifié CSPO, je maîtrise les cadres méthodologiques Agile et SAFe.

Parfaitement bilingue, j'anime les ateliers de conception et présente régulièrement les feuilles de route produit aux parties prenantes, tant en français qu'en anglais, assurant ainsi une parfaite cohésion entre les équipes techniques et les objectifs d'affaires à l'échelle nationale.

Je vous remercie de l'attention portée à mon dossier et me tiens à votre disposition pour une entrevue.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Marc-André Roy`
      },
      interview: [
        { q: "How do you approach prioritizing a product backlog with conflicting demands from business stakeholders and engineering teams?", lang: "en" },
        { q: "Comment décririez-vous l'importance d'une bonne conception d'API pour l'expérience des développeurs partenaires ?", lang: "fr" },
        { q: "Can you give an example of a time you had to explain a complex technical limitation to a non-technical corporate client?", lang: "en" },
        { q: "Comment gérez-vous l'alignement entre des équipes situées à Montréal (francophones) et à Toronto (anglophones) ?", lang: "fr" },
        { q: "Explain your experience with Agile frameworks. What is your role during backlog grooming?", lang: "en" }
      ],
      checklist: [
        "Align product roadmap terminology with RBC's digital banking standards",
        "Review Scaled Agile Framework (SAFe) product owner guidelines",
        "Prepare bilingual presentations demonstrating fintech API capabilities",
        "Draft the Bilingual Hybrid cover letter proving client-facing executive presence",
        "Practice answering API design questions in English and team leadership questions in French",
        "Verify travel requirements between Toronto and Montreal offices"
      ]
    }
  }
};

// --- BILINGUAL TECH GLOSSARY DATABASE ---
const GLOSSARY_DATA = [
  { en: "Full-Stack Developer", fr: "Développeur(euse) Full-Stack / Polyvalent(e)", ctx: "The English term is widely accepted in Quebec tech, but OQLF officially recommends 'développeur polyvalent'. Use 'Full-Stack' in private tech, 'polyvalent' in government/public sector.", cat: "role" },
  { en: "Product Owner", fr: "Propriétaire de produit (PO)", ctx: "Always translate in official French resumes, but 'Product Owner' is frequently used verbally in standups.", cat: "role" },
  { en: "Scrum Master", fr: "Facilitateur(trice) Scrum / Scrum Master", ctx: "OQLF suggests 'facilitateur'. In practice, both are used, but 'Scrum Master' is common in job descriptions.", cat: "role" },
  { en: "Cloud Computing", fr: "Infonuagique / Informatique en nuage", ctx: "Highly recommended to use 'infonuagique' in Quebec. It sounds extremely professional and is the official standard.", cat: "tech" },
  { en: "Framework", fr: "Cadre d'application / Framework", ctx: "'Cadre d'application' is the formal term, but developers almost exclusively say 'framework' in conversation.", cat: "tech" },
  { en: "Deployment", fr: "Déploiement", ctx: "Always translate. Never say 'deployment' in a French sentence; use 'déploiement' (e.g., 'pipeline de déploiement').", cat: "tech" },
  { en: "Feature", fr: "Fonctionnalité / Caractéristique", ctx: "Translate to 'fonctionnalité' when referring to a software feature. 'Feature' is considered anglicism in French.", cat: "tech" },
  { en: "Daily Standup", fr: "Mêlée quotidienne", ctx: "The official Agile term in French. Using 'mêlée quotidienne' in a French interview demonstrates strong local Agile fluency.", cat: "agile" },
  { en: "Product Backlog", fr: "Carnet de produit", ctx: "Always use 'carnet de produit' in French documents. 'Backlog' is common verbally, but 'carnet' is preferred.", cat: "agile" },
  { en: "Sprint Planning", fr: "Planification de sprint", ctx: "Standard translation. Smoothly blends the English word 'sprint' (which is accepted) with French structure.", cat: "agile" },
  { en: "User Story", fr: "Récit utilisateur", ctx: "Highly recommended to write 'récit utilisateur' in French specifications and resumes.", cat: "agile" },
  { en: "Database", fr: "Base de données", ctx: "Always translate. 'Database' should not be used in French writing.", cat: "tech" },
  { en: "Backend / Frontend", fr: "Dorsal / Frontal (ou Backend / Frontend)", ctx: "Public sector prefers 'dorsal/frontal'. Private tech companies in Montreal happily accept 'backend/frontend'.", cat: "role" },
  { en: "Technical Debt", fr: "Dette technique", ctx: "Direct translation, widely used and expected in both languages.", cat: "agile" }
];

// --- APP STATE ---
const STATE = {
  currentTemplate: "shopify",
  activeLang: "bilingual",
  resumeLanguage: "en",
  coverLetterStyle: "hybrid",
  pitchLanguage: "bilingual",
  geminiApiKey: localStorage.getItem("applywise_gemini_api_key") || "",
  geminiModel: localStorage.getItem("applywise_gemini_model") || "gemini-2.5-flash",
  
  // Custom user input state
  customJd: "",
  customResume: "",
  
  // Active analysis results (defaults to Shopify)
  analysis: JOB_TEMPLATES.shopify.analysis,
  
  // Interview state
  interview: {
    currentQuestionIndex: 0,
    messages: []
  },
  
  // Checklist state
  checklist: [...JOB_TEMPLATES.shopify.analysis.checklist],
  
  // Speech Practice State
  speech: {
    isRecording: false,
    mediaRecorder: null,
    audioChunks: [],
    startTime: null,
    timerInterval: null,
    recognition: null,
    transcript: ""
  }
};

// --- DOM ELEMENTS ---
const DOM = {
  // Navigation
  navItems: document.querySelectorAll(".nav-item"),
  panels: document.querySelectorAll(".panel"),
  themeToggleBtn: document.getElementById("theme-toggle-btn"),
  currentTemplateDisplay: document.getElementById("current-template-display"),
  langBtns: document.querySelectorAll(".lang-btn"),
  
  // Settings Modal
  openSettingsBtn: document.getElementById("open-settings-btn"),
  closeSettingsBtn: document.getElementById("close-settings-btn"),
  settingsModal: document.getElementById("settings-modal"),
  saveSettingsBtn: document.getElementById("save-settings-btn"),
  clearApiKeyBtn: document.getElementById("clear-api-key-btn"),
  geminiApiKeyInput: document.getElementById("gemini-api-key"),
  geminiModelSelect: document.getElementById("gemini-model-select"),
  apiStatusPill: document.getElementById("api-status-pill"),
  
  // Inputs
  templateCards: document.querySelectorAll(".template-card"),
  jdInput: document.getElementById("job-description-input"),
  resumeInput: document.getElementById("resume-input"),
  jdWordCount: document.getElementById("jd-word-count"),
  resumeWordCount: document.getElementById("resume-word-count"),
  analyzeBtn: document.getElementById("analyze-btn"),
  
  // Analytics Panel
  matchScoreText: document.getElementById("match-score-text"),
  scoreGaugeFill: document.getElementById("score-gauge-fill"),
  matchVerdict: document.getElementById("match-verdict"),
  techScoreVal: document.getElementById("tech-score-val"),
  techScoreBar: document.getElementById("tech-score-bar"),
  langScoreVal: document.getElementById("lang-score-val"),
  langScoreBar: document.getElementById("lang-score-bar"),
  expScoreVal: document.getElementById("exp-score-val"),
  expScoreBar: document.getElementById("exp-score-bar"),
  techSkillsMatrix: document.getElementById("tech-skills-matrix"),
  langSkillsMatrix: document.getElementById("lang-skills-matrix"),
  gapsList: document.getElementById("gaps-list"),
  academyRecommendations: document.getElementById("academy-recommendations"),
  
  // Resume Panel
  resumeBtnEn: document.getElementById("resume-btn-en"),
  resumeBtnFr: document.getElementById("resume-btn-fr"),
  resumeBulletsContainer: document.getElementById("resume-bullets-container"),
  copyResumeBtn: document.getElementById("copy-resume-btn"),
  
  // Cover Letter Panel
  coverLetterText: document.getElementById("cover-letter-text"),
  copyLetterBtn: document.getElementById("copy-letter-btn"),
  downloadLetterBtn: document.getElementById("download-letter-btn"),
  letterStyleRadios: document.getElementsByName("letter-style"),
  
  // Pitch Panel
  pitchTabBilingual: document.getElementById("pitch-tab-bilingual"),
  pitchTabEn: document.getElementById("pitch-tab-en"),
  pitchTabFr: document.getElementById("pitch-tab-fr"),
  pitchTextDisplay: document.getElementById("pitch-text-display"),
  pitchTipText: document.getElementById("pitch-tip-text"),
  recordPitchBtn: document.getElementById("record-pitch-btn"),
  recordBtnText: document.getElementById("record-btn-text"),
  recordingTimer: document.getElementById("recording-timer"),
  speechTranscript: document.getElementById("speech-transcript"),
  metricPaceVal: document.getElementById("metric-pace-val"),
  metricPaceBar: document.getElementById("metric-pace-bar"),
  metricFluencyVal: document.getElementById("metric-fluency-val"),
  metricFluencyBar: document.getElementById("metric-fluency-bar"),
  speechFeedbackText: document.getElementById("speech-feedback-text"),
  
  // Interview Panel
  intCompanyName: document.getElementById("int-company-name"),
  intFocusName: document.getElementById("int-focus-name"),
  intQuestionNum: document.getElementById("int-question-num"),
  resetInterviewBtn: document.getElementById("reset-interview-btn"),
  interviewQuestionList: document.getElementById("interview-question-list"),
  chatMessages: document.getElementById("chat-messages"),
  interviewUserInput: document.getElementById("interview-user-input"),
  interviewSendBtn: document.getElementById("interview-send-btn"),
  interviewSpeechBtn: document.getElementById("interview-speech-btn"),
  
  // Salary Panel
  salaryNumberInput: document.getElementById("salary-number-input"),
  salaryRangeInput: document.getElementById("salary-range-input"),
  salaryTableBody: document.getElementById("salary-table-body"),
  savingsChartContainer: document.getElementById("savings-chart-container"),
  
  // Glossary Panel
  glossarySearch: document.getElementById("glossary-search"),
  glossaryFilterBtns: document.querySelectorAll(".filter-options .btn"),
  glossaryTableBody: document.getElementById("glossary-table-body"),
  
  // Checklist Panel
  checklistDoneCount: document.getElementById("checklist-done-count"),
  checklistTotalCount: document.getElementById("checklist-total-count"),
  checklistProgressBar: document.getElementById("checklist-progress-bar"),
  checklistTodoList: document.getElementById("checklist-todo-list"),
  addTaskBtn: document.getElementById("add-task-btn")
};

// --- INITIALIZATION ---
function init() {
  setupEventListeners();
  loadTemplate(STATE.currentTemplate);
  updateApiStatusIndicator();
  renderGlossary();
  updateSalaryCalculator();
  
  // Load API keys from local storage
  if (STATE.geminiApiKey) {
    DOM.geminiApiKeyInput.value = STATE.geminiApiKey;
  }
  DOM.geminiModelSelect.value = STATE.geminiModel;
}

// --- EVENT LISTENERS ---
function setupEventListeners() {
  // Theme Toggle
  DOM.themeToggleBtn.addEventListener("click", toggleTheme);
  
  // Sidebar Navigation
  DOM.navItems.forEach(item => {
    item.addEventListener("click", () => {
      const targetTab = item.getAttribute("data-tab");
      switchTab(targetTab);
    });
  });
  
  // Language Selector (Top Right)
  DOM.langBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      DOM.langBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      STATE.activeLang = btn.getAttribute("data-lang");
      applyLanguageMode();
    });
  });

  // Settings Modal
  DOM.openSettingsBtn.addEventListener("click", () => DOM.settingsModal.classList.add("active"));
  DOM.closeSettingsBtn.addEventListener("click", () => DOM.settingsModal.classList.remove("active"));
  DOM.saveSettingsBtn.addEventListener("click", saveSettings);
  DOM.clearApiKeyBtn.addEventListener("click", clearApiKey);
  DOM.settingsModal.addEventListener("click", (e) => {
    if (e.target === DOM.settingsModal) DOM.settingsModal.classList.remove("active");
  });

  // Template Selection
  DOM.templateCards.forEach(card => {
    card.addEventListener("click", () => {
      DOM.templateCards.forEach(c => c.classList.remove("active"));
      card.classList.add("active");
      const templateName = card.getAttribute("data-template");
      STATE.currentTemplate = templateName;
      loadTemplate(templateName);
    });
  });

  // Word Counters
  DOM.jdInput.addEventListener("input", () => {
    const words = DOM.jdInput.value.trim().split(/\s+/).filter(Boolean).length;
    DOM.jdWordCount.textContent = `${words} words`;
    STATE.customJd = DOM.jdInput.value;
  });

  DOM.resumeInput.addEventListener("input", () => {
    const words = DOM.resumeInput.value.trim().split(/\s+/).filter(Boolean).length;
    DOM.resumeWordCount.textContent = `${words} words`;
    STATE.customResume = DOM.resumeInput.value;
  });

  // Analyze Button
  DOM.analyzeBtn.addEventListener("click", triggerAnalysis);

  // Resume Panel Toggles
  DOM.resumeBtnEn.addEventListener("click", () => {
    DOM.resumeBtnEn.classList.add("active");
    DOM.resumeBtnFr.classList.remove("active");
    STATE.resumeLanguage = "en";
    renderResumeBullets();
  });

  DOM.resumeBtnFr.addEventListener("click", () => {
    DOM.resumeBtnEn.classList.remove("active");
    DOM.resumeBtnFr.classList.add("active");
    STATE.resumeLanguage = "fr";
    renderResumeBullets();
  });

  DOM.copyResumeBtn.addEventListener("click", copyTailoredBullets);

  // Cover Letter Panel
  DOM.copyLetterBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(DOM.coverLetterText.innerText);
    showToast("Cover letter copied to clipboard!");
  });
  
  DOM.downloadLetterBtn.addEventListener("click", downloadCoverLetter);

  DOM.letterStyleRadios.forEach(radio => {
    radio.addEventListener("change", (e) => {
      STATE.coverLetterStyle = e.target.value;
      renderCoverLetter();
    });
  });

  // Pitch Panel Toggles
  DOM.pitchTabBilingual.addEventListener("click", () => setPitchLanguage("bilingual"));
  DOM.pitchTabEn.addEventListener("click", () => setPitchLanguage("en"));
  DOM.pitchTabFr.addEventListener("click", () => setPitchLanguage("fr"));
  DOM.recordPitchBtn.addEventListener("click", togglePitchRecording);

  // Interview Panel
  DOM.resetInterviewBtn.addEventListener("click", resetInterview);
  DOM.interviewSendBtn.addEventListener("click", sendInterviewAnswer);
  DOM.interviewUserInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendInterviewAnswer();
    }
  });
  DOM.interviewSpeechBtn.addEventListener("click", triggerInterviewSpeech);

  // Salary Calculator Inputs
  DOM.salaryNumberInput.addEventListener("input", (e) => {
    const val = parseInt(e.target.value) || 0;
    DOM.salaryRangeInput.value = val;
    updateSalaryCalculator();
  });

  DOM.salaryRangeInput.addEventListener("input", (e) => {
    const val = e.target.value;
    DOM.salaryNumberInput.value = val;
    updateSalaryCalculator();
  });

  // Glossary Search & Filter
  DOM.glossarySearch.addEventListener("input", renderGlossary);
  DOM.glossaryFilterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      DOM.glossaryFilterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      renderGlossary();
    });
  });

  // Checklist Panel
  DOM.addTaskBtn.addEventListener("click", addCustomTask);
}

// --- THEME MANAGEMENT ---
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute("data-theme");
  const newTheme = currentTheme === "light" ? "dark" : "light";
  document.documentElement.setAttribute("data-theme", newTheme);
  
  const sunIcon = DOM.themeToggleBtn.querySelector(".sun-icon");
  const moonIcon = DOM.themeToggleBtn.querySelector(".moon-icon");
  
  if (newTheme === "light") {
    sunIcon.style.display = "none";
    moonIcon.style.display = "block";
  } else {
    sunIcon.style.display = "block";
    moonIcon.style.display = "none";
  }
}

// --- TAB ROUTING ---
function switchTab(tabId) {
  DOM.panels.forEach(panel => panel.classList.remove("active"));
  DOM.navItems.forEach(item => item.classList.remove("active"));
  
  const activePanel = document.getElementById(tabId);
  if (activePanel) activePanel.classList.add("active");
  
  const activeNavItem = document.querySelector(`.nav-item[data-tab="${tabId}"]`);
  if (activeNavItem) activeNavItem.classList.add("active");
  
  // Smooth scroll to top of panel
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// --- SETTINGS & GEMINI API KEY ---
function saveSettings() {
  const apiKey = DOM.geminiApiKeyInput.value.trim();
  const model = DOM.geminiModelSelect.value;
  
  STATE.geminiApiKey = apiKey;
  STATE.geminiModel = model;
  
  localStorage.setItem("applywise_gemini_api_key", apiKey);
  localStorage.setItem("applywise_gemini_model", model);
  
  updateApiStatusIndicator();
  DOM.settingsModal.classList.remove("active");
  showToast("Settings saved successfully!");
}

function clearApiKey() {
  STATE.geminiApiKey = "";
  DOM.geminiApiKeyInput.value = "";
  localStorage.removeItem("applywise_gemini_api_key");
  updateApiStatusIndicator();
  DOM.settingsModal.classList.remove("active");
  showToast("API Key removed.");
}

function updateApiStatusIndicator() {
  const dot = DOM.apiStatusPill.querySelector(".api-status-dot");
  const text = DOM.apiStatusPill.querySelector(".api-status-text");
  
  if (STATE.geminiApiKey) {
    dot.className = "api-status-dot online";
    text.textContent = "Gemini Live";
    DOM.apiStatusPill.setAttribute("title", `Connected to ${STATE.geminiModel}`);
  } else {
    dot.className = "api-status-dot offline";
    text.textContent = "Simulated AI";
    DOM.apiStatusPill.setAttribute("title", "Running in offline simulation mode using pre-compiled analysis");
  }
}

// --- TEMPLATE LOADING ---
function loadTemplate(name) {
  const template = JOB_TEMPLATES[name];
  if (!template) return;
  
  DOM.jdInput.value = template.jd;
  DOM.resumeInput.value = template.resume;
  
  // Update word counts
  DOM.jdInput.dispatchEvent(new Event("input"));
  DOM.resumeInput.dispatchEvent(new Event("input"));
  
  DOM.currentTemplateDisplay.textContent = `Active Profile: ${template.company} - ${template.role}`;
  
  // Load analysis and update panels
  STATE.analysis = template.analysis;
  STATE.checklist = [...template.analysis.checklist];
  
  updateAllPanels();
}

function updateAllPanels() {
  renderAnalytics();
  renderResumeBullets();
  renderCoverLetter();
  renderPitch();
  initInterview();
  renderChecklist();
}

// --- ANALYTICS PANEL RENDER ---
function renderAnalytics() {
  const analysis = STATE.analysis;
  
  // Animate Gauge
  DOM.matchScoreText.textContent = `${analysis.score}%`;
  DOM.matchVerdict.textContent = analysis.verdict;
  
  // Classify verdict style
  if (analysis.score >= 90) {
    DOM.matchVerdict.className = "match-verdict text-green";
  } else if (analysis.score >= 75) {
    DOM.matchVerdict.className = "match-verdict text-teal";
  } else {
    DOM.matchVerdict.className = "match-verdict text-yellow";
  }
  
  // SVG Stroke animation: circle circumference is 2 * PI * r = 2 * 3.1415 * 50 = 314
  const offset = 314 - (314 * analysis.score) / 100;
  DOM.scoreGaugeFill.style.strokeDashoffset = offset;
  
  // Adjust stroke color based on score
  if (analysis.score >= 90) {
    DOM.scoreGaugeFill.style.stroke = "var(--accent-green)";
  } else if (analysis.score >= 75) {
    DOM.scoreGaugeFill.style.stroke = "var(--primary-color)";
  } else {
    DOM.scoreGaugeFill.style.stroke = "var(--accent-yellow)";
  }

  // Update Breakdown Progress Bars
  DOM.techScoreVal.textContent = `${analysis.techScore}%`;
  DOM.techScoreBar.style.width = `${analysis.techScore}%`;
  
  DOM.langScoreVal.textContent = `${analysis.langScore}%`;
  DOM.langScoreBar.style.width = `${analysis.langScore}%`;
  
  DOM.expScoreVal.textContent = `${analysis.expScore}%`;
  DOM.expScoreBar.style.width = `${analysis.expScore}%`;

  // Render Technical Skills Matrix
  DOM.techSkillsMatrix.innerHTML = analysis.techSkills.map(skill => `
    <li>
      <svg class="skill-status-icon ${skill.match ? 'text-green' : 'text-muted'}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
        ${skill.match ? '<polyline points="20 6 9 17 4 12"/>' : '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>'}
      </svg>
      <span>
        <strong>${skill.name}</strong> 
        ${skill.note ? `<br><small style="color: var(--text-secondary)">${skill.note}</small>` : ''}
      </span>
    </li>
  `).join("");

  // Render Language Skills Matrix
  DOM.langSkillsMatrix.innerHTML = analysis.langSkills.map(skill => `
    <li>
      <svg class="skill-status-icon ${skill.match ? 'text-green' : 'text-muted'}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
        ${skill.match ? '<polyline points="20 6 9 17 4 12"/>' : '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>'}
      </svg>
      <span>
        <strong>${skill.name}</strong>
        ${skill.note ? `<br><small style="color: var(--text-secondary)">${skill.note}</small>` : ''}
      </span>
    </li>
  `).join("");

  // Render Gaps & Actions
  DOM.gapsList.innerHTML = analysis.gaps.map(gap => `
    <div class="gap-item">
      <svg class="gap-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
        <line x1="12" y1="9" x2="12" y2="13"/>
        <line x1="12" y1="17" x2="12.01" y2="17"/>
      </svg>
      <div class="gap-details">
        <div class="gap-title">${gap.title}</div>
        <div class="gap-action"><strong>Action:</strong> ${gap.action}</div>
      </div>
    </div>
  `).join("");

  // Render Academy Recommendations
  DOM.academyRecommendations.innerHTML = analysis.academy.map(item => `
    <div class="academy-item">
      <span class="academy-provider">${item.provider}</span>
      <div class="academy-title">${item.title}</div>
      <div class="academy-desc">${item.desc}</div>
    </div>
  `).join("");
}

// --- RESUME TAILOR PANEL RENDER ---
function renderResumeBullets() {
  const lang = STATE.resumeLanguage;
  const bullets = STATE.analysis.bullets[lang];
  
  if (!bullets) return;

  DOM.resumeBulletsContainer.innerHTML = bullets.map(b => `
    <div class="bullet-comparison-row">
      <div class="bullet-original">${b.original}</div>
      <div class="bullet-tailored">${highlightKeywords(b.tailored)}</div>
    </div>
  `).join("");
}

function highlightKeywords(text) {
  // Regex to highlight specific tech terms or action verbs
  // Highlight English keywords
  let highlighted = text.replace(
    /\b(Architected|Collaborated|Developed|Built|Optimized|React|Redux|Ruby on Rails|PostgreSQL|GraphQL|APIs|Agile|Scrum)\b/gi,
    match => `<span class="keyword-highlight">${match}</span>`
  );
  
  // Highlight French keywords
  highlighted = highlighted.replace(
    /\b(Conçu|Optimisé|Développé|Collaboré|bilingues|bilingue|anglais|français|communiquer|mêlées quotidiennes|planifications|technique)\b/gi,
    match => `<span class="lang-highlight">${match}</span>`
  );
  
  return highlighted;
}

function copyTailoredBullets() {
  const lang = STATE.resumeLanguage;
  const bullets = STATE.analysis.bullets[lang];
  const bulletText = bullets.map(b => `• ${b.tailored}`).join("\n");
  
  navigator.clipboard.writeText(bulletText);
  showToast(`Tailored ${lang === 'en' ? 'English' : 'French'} bullets copied!`);
}

// --- COVER LETTER PANEL RENDER ---
function renderCoverLetter() {
  const style = STATE.coverLetterStyle;
  const letter = STATE.analysis.coverLetters[style] || STATE.analysis.coverLetters['hybrid'];
  DOM.coverLetterText.innerText = letter;
}

function downloadCoverLetter() {
  const style = STATE.coverLetterStyle;
  const letter = DOM.coverLetterText.innerText;
  const blob = new Blob([letter], { type: "text/plain;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  
  const a = document.createElement("a");
  a.href = url;
  a.download = `ApplyWise_CoverLetter_${style}.txt`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// --- PITCH COACH PANEL RENDER ---
function setPitchLanguage(lang) {
  DOM.pitchTabBilingual.classList.remove("active");
  DOM.pitchTabEn.classList.remove("active");
  DOM.pitchTabFr.classList.remove("active");
  
  if (lang === "bilingual") DOM.pitchTabBilingual.classList.add("active");
  if (lang === "en") DOM.pitchTabEn.classList.add("active");
  if (lang === "fr") DOM.pitchTabFr.classList.add("active");
  
  STATE.pitchLanguage = lang;
  renderPitch();
}

function renderPitch() {
  const lang = STATE.pitchLanguage;
  const pitch = STATE.analysis.pitches[lang];
  DOM.pitchTextDisplay.textContent = pitch;
  
  // Context-specific tips
  if (lang === "bilingual") {
    DOM.pitchTipText.innerHTML = `<strong>Bilingual Transition Tip:</strong> Swap languages at a natural transition point, such as moving from your technical stack (often in English) to your collaboration and client-facing skills (highly valued in French). Keep the flow smooth!`;
  } else if (lang === "fr") {
    DOM.pitchTipText.innerHTML = `<strong>Conseil d'entretien en français :</strong> Use terms like <em>"mêlée quotidienne"</em> (daily standup) and <em>"cadre d'application"</em> (framework) to showcase sophisticated, professional French communication suitable for Canadian tech hubs.`;
  } else {
    DOM.pitchTipText.innerHTML = `<strong>English Delivery Tip:</strong> Highlight how your bilingualism helps you bridge teams across different offices in Canada (e.g., Montreal and Toronto/Vancouver). Emphasize it as an operational advantage.`;
  }
}

// --- SPEECH PRACTICE SANDBOX ---
function togglePitchRecording() {
  if (STATE.speech.isRecording) {
    stopPitchRecording();
  } else {
    startPitchRecording();
  }
}

function startPitchRecording() {
  STATE.speech.isRecording = true;
  DOM.recordPitchBtn.classList.add("recording");
  DOM.recordBtnText.textContent = "Recording...";
  DOM.recordingTimer.textContent = "00:00 / 00:30";
  DOM.speechTranscript.textContent = "Listening... Start reading your pitch.";
  
  // Set up timer
  STATE.speech.startTime = Date.now();
  STATE.speech.timerInterval = setInterval(() => {
    const elapsed = Math.floor((Date.now() - STATE.speech.startTime) / 1000);
    const secs = String(elapsed % 60).padStart(2, "0");
    const mins = String(Math.floor(elapsed / 60)).padStart(2, "0");
    DOM.recordingTimer.textContent = `${mins}:${secs} / 00:30`;
    
    if (elapsed >= 30) {
      stopPitchRecording();
    }
  }, 1000);

  // Speech Recognition (Web Speech API)
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    const rec = new SpeechRecognition();
    rec.continuous = true;
    rec.interimResults = true;
    rec.lang = STATE.pitchLanguage === "fr" ? "fr-CA" : "en-CA";
    
    rec.onresult = (event) => {
      let interimTranscript = '';
      let finalTranscript = '';
      
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          finalTranscript += event.results[i][0].transcript;
        } else {
          interimTranscript += event.results[i][0].transcript;
        }
      }
      
      DOM.speechTranscript.textContent = finalTranscript || interimTranscript || "Reading pitch...";
      STATE.speech.transcript = finalTranscript || interimTranscript;
    };

    rec.onerror = (e) => {
      console.warn("Speech recognition error:", e.error);
    };

    STATE.speech.recognition = rec;
    rec.start();
  } else {
    DOM.speechTranscript.textContent = "Web Speech API is not fully supported in this browser. (Simulating recording...)";
  }
}

function stopPitchRecording() {
  STATE.speech.isRecording = false;
  DOM.recordPitchBtn.classList.remove("recording");
  DOM.recordBtnText.textContent = "Start Speaking";
  clearInterval(STATE.speech.timerInterval);
  
  if (STATE.speech.recognition) {
    STATE.speech.recognition.stop();
  }
  
  // Calculate delivery metrics
  evaluateSpeechDelivery();
}

function evaluateSpeechDelivery() {
  const elapsed = Math.floor((Date.now() - STATE.speech.startTime) / 1000);
  if (elapsed < 3) {
    DOM.speechTranscript.textContent = "Recording was too short. Please try again!";
    return;
  }

  // Generate simulated or semi-parsed feedback
  let transcript = STATE.speech.transcript || DOM.pitchTextDisplay.textContent;
  const words = transcript.split(/\s+/).filter(Boolean).length;
  const wpm = Math.round((words / elapsed) * 60);
  
  // Pace Rating
  let paceText = "Good";
  let pacePercent = 85;
  if (wpm < 110) {
    paceText = "Too Slow";
    pacePercent = 50;
  } else if (wpm > 160) {
    paceText = "Too Fast";
    pacePercent = 60;
  }
  
  DOM.metricPaceVal.textContent = `${wpm} WPM (${paceText})`;
  DOM.metricPaceBar.style.width = `${pacePercent}%`;

  // Fluency Rating
  let fluencyPercent = 75;
  let fluencyText = "Intermediate";
  
  // Count bilingual transitions if bilingual pitch
  if (STATE.pitchLanguage === "bilingual") {
    // Look for both English and French words
    const hasEnglish = /\b(the|and|experience|React|Rails|developer)\b/i.test(transcript);
    const hasFrench = /\b(je|suis|développeur|bilingue|équipe|Montréal|Ottawa)\b/i.test(transcript);
    
    if (hasEnglish && hasFrench) {
      fluencyText = "Excellent Bilingual Transition";
      fluencyPercent = 95;
    } else {
      fluencyText = "Single Language Detected";
      fluencyPercent = 65;
    }
  } else {
    fluencyText = "Fluent & Steady";
    fluencyPercent = 90;
  }
  
  DOM.metricFluencyVal.textContent = fluencyText;
  DOM.metricFluencyBar.style.width = `${fluencyPercent}%`;

  // Feedback Text
  if (STATE.pitchLanguage === "bilingual") {
    DOM.speechFeedbackText.innerHTML = `🏁 **Delivery Report**: Your speaking pace was **${wpm} WPM**. You successfully transitioned between English and French. Try to keep your posture upright and pronounce the technical terms clearly in English while maintaining a natural, warm accent in French.`;
  } else {
    DOM.speechFeedbackText.innerHTML = `🏁 **Delivery Report**: Your speaking pace was **${wpm} WPM**. Great clarity. Ensure you emphasize the action verbs and pause slightly after key achievements to let them sink in with the recruiter.`;
  }
}

// --- BILINGUAL INTERVIEW PREP ---
function initInterview() {
  const analysis = STATE.analysis;
  
  // Set meta
  DOM.intCompanyName.textContent = STATE.currentTemplate === "custom" ? "Custom Target" : JOB_TEMPLATES[STATE.currentTemplate].company;
  DOM.intFocusName.textContent = STATE.activeLang === "bilingual" ? "Bilingual Tech" : (STATE.activeLang === "fr" ? "Français" : "English");
  
  STATE.interview.currentQuestionIndex = 0;
  STATE.interview.messages = [];
  
  // Render Question List Sidebar
  DOM.interviewQuestionList.innerHTML = analysis.interview.map((q, idx) => `
    <li class="question-item ${idx === 0 ? 'active' : ''}" data-idx="${idx}" id="int-q-item-${idx}">
      Question ${idx + 1} (${q.lang === 'bilingual' ? 'EN/FR' : q.lang.toUpperCase()})
    </li>
  `).join("");
  
  // Clear chat
  DOM.chatMessages.innerHTML = "";
  
  // Add first bot message
  addBotMessage(analysis.interview[0].q);
  updateInterviewSidebar();
}

function updateInterviewSidebar() {
  DOM.intQuestionNum.textContent = `${STATE.interview.currentQuestionIndex + 1} of ${STATE.analysis.interview.length}`;
  
  // Update active question item
  for (let i = 0; i < STATE.analysis.interview.length; i++) {
    const item = document.getElementById(`int-q-item-${i}`);
    if (item) {
      item.classList.remove("active");
      if (i === STATE.interview.currentQuestionIndex) {
        item.classList.add("active");
      }
      if (i < STATE.interview.currentQuestionIndex) {
        item.classList.add("completed");
      }
    }
  }
}

function addBotMessage(text) {
  const msg = { sender: "bot", text, timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) };
  STATE.interview.messages.push(msg);
  
  const msgEl = document.createElement("div");
  msgEl.className = "message bot";
  msgEl.innerHTML = `
    <div class="message-bubble">${text}</div>
    <div class="message-meta">${msg.timestamp} • AI Recruiter</div>
  `;
  
  DOM.chatMessages.appendChild(msgEl);
  DOM.chatMessages.scrollTop = DOM.chatMessages.scrollHeight;
}

function addUserMessage(text) {
  const msg = { sender: "user", text, timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) };
  STATE.interview.messages.push(msg);
  
  const msgEl = document.createElement("div");
  msgEl.className = "message user";
  msgEl.innerHTML = `
    <div class="message-bubble">${text}</div>
    <div class="message-meta">${msg.timestamp} • You</div>
  `;
  
  DOM.chatMessages.appendChild(msgEl);
  DOM.chatMessages.scrollTop = DOM.chatMessages.scrollHeight;
}

async function sendInterviewAnswer() {
  const text = DOM.interviewUserInput.value.trim();
  if (!text) return;
  
  DOM.interviewUserInput.value = "";
  addUserMessage(text);
  
  // Simulate bot typing/thinking
  const loader = document.createElement("div");
  loader.className = "message bot typing-loader";
  loader.innerHTML = `<div class="message-bubble">Analyzing your answer...</div>`;
  DOM.chatMessages.appendChild(loader);
  DOM.chatMessages.scrollTop = DOM.chatMessages.scrollHeight;

  // Generate feedback (live or simulated)
  let feedback = "";
  if (STATE.geminiApiKey) {
    feedback = await getLiveInterviewFeedback(STATE.analysis.interview[STATE.interview.currentQuestionIndex].q, text);
  } else {
    // Simulated Feedback based on length and keywords
    await new Promise(r => setTimeout(r, 1500)); // Simulate delay
    feedback = generateSimulatedFeedback(text);
  }

  loader.remove();

  // Render Feedback
  const feedbackEl = document.createElement("div");
  feedbackEl.className = "feedback-bubble";
  feedbackEl.innerHTML = `
    <h5>💡 Interviewer Feedback & Coaching</h5>
    <div>${feedback}</div>
  `;
  DOM.chatMessages.appendChild(feedbackEl);

  // Move to next question or conclude
  STATE.interview.currentQuestionIndex++;
  
  if (STATE.interview.currentQuestionIndex < STATE.analysis.interview.length) {
    updateInterviewSidebar();
    // Ask next question
    addBotMessage(STATE.analysis.interview[STATE.interview.currentQuestionIndex].q);
  } else {
    // Conclude Interview
    updateInterviewSidebar();
    addBotMessage("Thank you! We have completed the mock interview. You have done a great job practicing. Review the feedback cards in the chat history to improve your answers!");
  }
  
  DOM.chatMessages.scrollTop = DOM.chatMessages.scrollHeight;
}

function generateSimulatedFeedback(answer) {
  const words = answer.split(/\s+/).filter(Boolean).length;
  
  // Check languages
  const hasEnglish = /[a-zA-Z]/g.test(answer) && !/\b(le|la|les|un|une|et|en|je|suis|est)\b/i.test(answer);
  const hasFrench = /\b(je|suis|est|et|un|une|le|la|les|pour|dans|avec)\b/i.test(answer);
  
  let languageReview = "";
  if (hasEnglish && hasFrench) {
    languageReview = "Excellent use of bilingual transitions. You integrated technical terminology in English while explaining context in French smoothly.";
  } else if (hasFrench) {
    languageReview = "Good French response. Try to ensure you use standardized Canadian tech terms (e.g. 'mêlée' instead of 'standup') to sound more polished.";
  } else {
    languageReview = "Clear English answer. For a bilingual role, consider introducing yourself or summarizing your achievements in French to showcase written adaptability.";
  }

  let techReview = "";
  if (words < 15) {
    techReview = "Your answer was a bit short. Try using the **STAR method** (Situation, Task, Action, Result) to expand on your experience.";
  } else {
    techReview = "Strong detail. You mentioned specific technologies and frameworks. Make sure to link the result back to business value (e.g., 'reducing load times by 20%').";
  }

  return `
    <p><strong>Language Fluency:</strong> ${languageReview}</p>
    <p style="margin-top: 6px;"><strong>Content & Structure:</strong> ${techReview}</p>
  `;
}

function resetInterview() {
  initInterview();
  showToast("Interview simulator reset!");
}

function triggerInterviewSpeech() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    showToast("Speech recognition not supported in this browser.");
    return;
  }

  const rec = new SpeechRecognition();
  rec.lang = STATE.analysis.interview[STATE.interview.currentQuestionIndex].lang === "fr" ? "fr-CA" : "en-CA";
  
  DOM.interviewSpeechBtn.classList.add("active");
  showToast("Listening... Speak your answer.");

  rec.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    DOM.interviewUserInput.value = transcript;
  };

  rec.onend = () => {
    DOM.interviewSpeechBtn.classList.remove("active");
  };

  rec.start();
}

// --- SALARY & COST OF LIVING CALCULATOR ---
const CITY_FINANCIALS = {
  toronto: { name: "Toronto (ON)", rent: 2500, expenses: 1200, provTaxKey: "ON" },
  vancouver: { name: "Vancouver (BC)", rent: 2700, expenses: 1250, provTaxKey: "BC" },
  montreal: { name: "Montreal (QC)", rent: 1650, expenses: 950, provTaxKey: "QC" },
  ottawa: { name: "Ottawa (ON)", rent: 2000, expenses: 1050, provTaxKey: "ON" },
  waterloo: { name: "Waterloo (ON)", rent: 1850, expenses: 1000, provTaxKey: "ON" }
};

function calculateTaxes(salary, province) {
  // Approximate 2026 Federal and Provincial Tax Calculations
  
  // 1. Federal Tax
  const fedBrackets = [
    { limit: 55867, rate: 0.15 },
    { limit: 111733, rate: 0.205 },
    { limit: 173205, rate: 0.26 },
    { limit: 246752, rate: 0.29 },
    { limit: Infinity, rate: 0.33 }
  ];
  
  let fedTax = 0;
  let remainingSalary = salary;
  let prevLimit = 0;
  
  for (const b of fedBrackets) {
    const currentBracketAmount = Math.min(remainingSalary, b.limit - prevLimit);
    fedTax += currentBracketAmount * b.rate;
    remainingSalary -= currentBracketAmount;
    if (remainingSalary <= 0) break;
    prevLimit = b.limit;
  }

  // 2. Provincial Tax
  let provTax = 0;
  remainingSalary = salary;
  prevLimit = 0;

  if (province === "ON") {
    const onBrackets = [
      { limit: 51446, rate: 0.0505 },
      { limit: 102894, rate: 0.0915 },
      { limit: 150000, rate: 0.1116 },
      { limit: 220000, rate: 0.1216 },
      { limit: Infinity, rate: 0.1316 }
    ];
    for (const b of onBrackets) {
      const currentBracketAmount = Math.min(remainingSalary, b.limit - prevLimit);
      provTax += currentBracketAmount * b.rate;
      remainingSalary -= currentBracketAmount;
      if (remainingSalary <= 0) break;
      prevLimit = b.limit;
    }
  } else if (province === "BC") {
    const bcBrackets = [
      { limit: 47579, rate: 0.0506 },
      { limit: 95160, rate: 0.077 },
      { limit: 109220, rate: 0.105 },
      { limit: 132654, rate: 0.1229 },
      { limit: 172602, rate: 0.147 },
      { limit: 252752, rate: 0.168 },
      { limit: Infinity, rate: 0.205 }
    ];
    for (const b of bcBrackets) {
      const currentBracketAmount = Math.min(remainingSalary, b.limit - prevLimit);
      provTax += currentBracketAmount * b.rate;
      remainingSalary -= currentBracketAmount;
      if (remainingSalary <= 0) break;
      prevLimit = b.limit;
    }
  } else if (province === "QC") {
    const qcBrackets = [
      { limit: 51780, rate: 0.14 },
      { limit: 103545, rate: 0.19 },
      { limit: 126000, rate: 0.24 },
      { limit: Infinity, rate: 0.2575 }
    ];
    for (const b of qcBrackets) {
      const currentBracketAmount = Math.min(remainingSalary, b.limit - prevLimit);
      provTax += currentBracketAmount * b.rate;
      remainingSalary -= currentBracketAmount;
      if (remainingSalary <= 0) break;
      prevLimit = b.limit;
    }
  }

  // CPP & EI (Approximate Employee maximums)
  const cpp = Math.min(salary * 0.0595, 4055);
  const ei = Math.min(salary * 0.0166, 1049);

  const totalTax = fedTax + provTax + cpp + ei;
  return totalTax;
}

function updateSalaryCalculator() {
  const salary = parseInt(DOM.salaryNumberInput.value) || 0;
  
  let tableHtml = "";
  let chartHtml = "";

  Object.keys(CITY_FINANCIALS).forEach(key => {
    const city = CITY_FINANCIALS[key];
    const yearlyTax = calculateTaxes(salary, city.provTaxKey);
    const netIncome = salary - yearlyTax;
    
    const monthlyNet = netIncome / 12;
    const monthlyRent = city.rent;
    const monthlyExpenses = city.expenses;
    const monthlySavings = Math.max(0, monthlyNet - monthlyRent - monthlyExpenses);

    // Percentages for stacked bar chart
    const taxPercent = (yearlyTax / salary) * 100;
    const rentPercent = ((monthlyRent * 12) / salary) * 100;
    const expPercent = ((monthlyExpenses * 12) / salary) * 100;
    const savingsPercent = 100 - taxPercent - rentPercent - expPercent;

    // Table Row
    tableHtml += `
      <tr>
        <td><strong>${city.name}</strong></td>
        <td>$${Math.round(netIncome).toLocaleString()}/yr<br><small style="color: var(--text-muted)">$${Math.round(monthlyNet).toLocaleString()}/mo</small></td>
        <td>$${monthlyRent.toLocaleString()}/mo</td>
        <td>$${monthlyExpenses.toLocaleString()}/mo</td>
        <td class="${monthlySavings > 2000 ? 'text-green' : (monthlySavings > 1000 ? 'text-teal' : 'text-yellow')}">
          <strong>$${Math.round(monthlySavings).toLocaleString()}/mo</strong>
        </td>
      </tr>
    `;

    // Chart Row
    chartHtml += `
      <div class="city-chart-row">
        <div class="chart-row-label">
          <span>${city.name}</span>
          <span class="text-green">$${Math.round(monthlySavings).toLocaleString()}/mo savings</span>
        </div>
        <div class="chart-row-bars">
          <div class="bar-segment tax" style="width: ${taxPercent}%" title="Taxes: ${Math.round(taxPercent)}%"></div>
          <div class="bar-segment rent" style="width: ${rentPercent}%" title="Rent: ${Math.round(rentPercent)}%"></div>
          <div class="bar-segment expenses" style="width: ${expPercent}%" title="Expenses: ${Math.round(expPercent)}%"></div>
          <div class="bar-segment savings" style="width: ${Math.max(0, savingsPercent)}%" title="Savings: ${Math.round(Math.max(0, savingsPercent))}%"></div>
        </div>
      </div>
    `;
  });

  DOM.salaryTableBody.innerHTML = tableHtml;
  DOM.savingsChartContainer.innerHTML = chartHtml;
}

// --- BILINGUAL TECH GLOSSARY RENDER ---
function renderGlossary() {
  const query = DOM.glossarySearch.value.trim().toLowerCase();
  
  // Get active filter
  let activeFilter = "all";
  DOM.glossaryFilterBtns.forEach(btn => {
    if (btn.classList.contains("active")) {
      activeFilter = btn.getAttribute("data-filter");
    }
  });

  const filtered = GLOSSARY_DATA.filter(item => {
    const matchesQuery = item.en.toLowerCase().includes(query) || item.fr.toLowerCase().includes(query) || item.ctx.toLowerCase().includes(query);
    const matchesFilter = activeFilter === "all" || item.cat === activeFilter;
    return matchesQuery && matchesFilter;
  });

  DOM.glossaryTableBody.innerHTML = filtered.map(item => `
    <tr>
      <td><strong>${item.en}</strong></td>
      <td class="text-teal"><strong>${item.fr}</strong></td>
      <td>${item.ctx}</td>
      <td><span class="glossary-badge badge-${item.cat}">${item.cat}</span></td>
    </tr>
  `).join("");
}

// --- APPLICATION CHECKLIST RENDER ---
function renderChecklist() {
  const checklist = STATE.checklist;
  DOM.checklistTotalCount.textContent = checklist.length;
  
  let doneCount = 0;
  
  DOM.checklistTodoList.innerHTML = checklist.map((task, idx) => {
    // Simple state tracking using data attributes or classes
    const isChecked = false; // By default loaded tasks are unchecked
    return `
      <li class="todo-item" id="todo-item-${idx}">
        <input type="checkbox" class="todo-checkbox" data-idx="${idx}" onchange="toggleTaskCheck(${idx}, this)">
        <span class="todo-label">${task}</span>
        <button class="delete-task-btn" onclick="deleteTask(${idx})">&times;</button>
      </li>
    `;
  }).join("");

  updateChecklistProgress();
}

window.toggleTaskCheck = function(idx, checkbox) {
  const row = document.getElementById(`todo-item-${idx}`);
  if (checkbox.checked) {
    row.classList.add("checked");
  } else {
    row.classList.remove("checked");
  }
  updateChecklistProgress();
};

window.deleteTask = function(idx) {
  STATE.checklist.splice(idx, 1);
  renderChecklist();
  showToast("Task deleted.");
};

function updateChecklistProgress() {
  const checkboxes = DOM.checklistTodoList.querySelectorAll(".todo-checkbox");
  let done = 0;
  checkboxes.forEach(c => {
    if (c.checked) done++;
  });
  
  DOM.checklistDoneCount.textContent = done;
  
  const total = checkboxes.length;
  const pct = total > 0 ? (done / total) * 100 : 0;
  DOM.checklistProgressBar.style.width = `${pct}%`;
}

function addCustomTask() {
  const taskText = prompt("Enter custom task description:");
  if (taskText && taskText.trim()) {
    STATE.checklist.push(taskText.trim());
    renderChecklist();
    showToast("Task added!");
  }
}

// --- SIMULATED AND LIVE ANALYSIS TRIGGER ---
async function triggerAnalysis() {
  const jd = DOM.jdInput.value.trim();
  const resume = DOM.resumeInput.value.trim();
  
  if (!jd || !resume) {
    alert("Please provide both the Job Description and your Resume/Profile to analyze.");
    return;
  }

  // Switch to Loader state
  DOM.analyzeBtn.disabled = true;
  DOM.analyzeBtn.querySelector("span").textContent = "Analyzing Application...";
  
  try {
    if (STATE.geminiApiKey) {
      // LIVE GEMINI AI ANALYSIS
      await runLiveGeminiAnalysis(jd, resume);
    } else {
      // LOCAL RULE-BASED CUSTOM ANALYSIS SIMULATOR
      await new Promise(r => setTimeout(r, 2000)); // Simulate AI analysis latency
      runLocalRuleBasedAnalysis(jd, resume);
    }
    
    // Switch to Analytics Panel to show results
    switchTab("analytics-panel");
    showToast("Analysis complete! Application package updated.");
  } catch (error) {
    console.error(error);
    alert("An error occurred during analysis: " + error.message);
  } finally {
    DOM.analyzeBtn.disabled = false;
    DOM.analyzeBtn.querySelector("span").textContent = "Analyze Application & Generate Package";
  }
}

// --- LOCAL RULE-BASED ANALYSIS ENGINE ---
function runLocalRuleBasedAnalysis(jd, resume) {
  // Perform basic client-side analysis
  const jdLower = jd.toLowerCase();
  const resumeLower = resume.toLowerCase();
  
  // Extract technical keyword matches
  const techKeywords = [
    { key: "react", name: "React / Frontend" },
    { key: "rails", name: "Ruby on Rails" },
    { key: "node", name: "Node.js" },
    { key: "python", name: "Python" },
    { key: "aws", name: "AWS Cloud" },
    { key: "kubernetes", name: "Kubernetes" },
    { key: "docker", name: "Docker & Conteneurs" },
    { key: "postgres", name: "PostgreSQL" },
    { key: "graphql", name: "GraphQL" },
    { key: "agile", name: "Agile / Scrum" }
  ];

  const techSkills = [];
  let matchedTechCount = 0;
  
  techKeywords.forEach(item => {
    if (jdLower.includes(item.key)) {
      const hasSkill = resumeLower.includes(item.key);
      if (hasSkill) matchedTechCount++;
      techSkills.push({
        name: item.name,
        match: hasSkill,
        note: hasSkill ? "Direct match found in resume." : `Required by job, but missing from resume.`
      });
    }
  });

  // Extract language requirements
  const hasFrenchJd = /\b(french|français|bilingue|bilingual)\b/i.test(jdLower);
  const hasFrenchResume = /\b(french|français|bilingue|bilingual|b1|b2|c1|c2|intermediate french)\b/i.test(resumeLower);
  
  const langSkills = [
    { name: "English (Technical Writing)", match: true },
    { name: "French (Bilingual Collaboration)", match: hasFrenchResume, note: hasFrenchResume ? "French competency declared in profile." : "Job requests bilingual capability, but French not mentioned in resume." }
  ];

  // Calculate scores
  const techScore = techSkills.length > 0 ? Math.round((matchedTechCount / techSkills.length) * 100) : 80;
  const langScore = hasFrenchJd ? (hasFrenchResume ? 95 : 50) : 100;
  const expScore = resumeLower.match(/\b(senior|lead|manager|5\+|6\+|7\+|8\+)\b/i) ? 90 : 75;
  const overallScore = Math.round((techScore * 0.5) + (langScore * 0.3) + (expScore * 0.2));

  // Determine gaps
  const gaps = [];
  techSkills.forEach(skill => {
    if (!skill.match) {
      gaps.push({
        title: `Technical Gap: ${skill.name}`,
        action: `Learn basic concepts and configure a sandbox environment for ${skill.name}.`
      });
    }
  });
  if (hasFrenchJd && !hasFrenchResume) {
    gaps.push({
      title: "Language Gap: French Communication",
      action: "Review tech industry terminology in French and practice conversational transitions."
    });
  }

  // Generate generic tailored bullets
  const bullets = {
    en: [
      { original: "Led development of key features in web applications.", tailored: "Architected modern web services, integrating robust APIs to improve page responsiveness." },
      { original: "Collaborated with team members to ship software.", tailored: "Collaborated in cross-functional Agile sprint cycles, delivering deliverables 15% ahead of schedule." }
    ],
    fr: [
      { original: "Dirigé le développement d'applications web.", tailored: "Conçu des architectures frontales dynamiques avec React, améliorant la réactivité de l'application." },
      { original: "Collaboré au sein de l'équipe pour livrer les logiciels.", tailored: "Collaboré au sein d'équipes Agile bilingues pour livrer des incréments de produit de haute qualité." }
    ]
  };

  // Generate cover letter
  const companyName = jd.match(/\b(Shopify|RBC|Coveo|OpenText|Rogers|Bell|Amazon|Google)\b/i)?.[0] || "Target Company";
  const roleName = jd.match(/\b(Developer|Engineer|Product Manager|Architect|Analyst)\b/i)?.[0] || "Technical Specialist";

  const hybridCoverLetter = `Candidate Name
City, Province
June 30, 2026

À l'attention du comité de recrutement
${companyName}

Objet : Candidature pour le poste de ${roleName} Bilingue

Madame, Monsieur,

C'est avec beaucoup d'enthousiasme que je soumets ma candidature pour le poste de ${roleName} chez ${companyName}. Intégrer vos équipes représente pour moi une formidable opportunité d'associer mon parcours technique à un environnement de travail bilingue et collaboratif.

I have spent the last few years developing robust software systems and collaborating with cross-functional product teams. In my previous work, I focused on building scalable services, improving database performance, and driving developer efficiency. I am excited to bring this technological foundation to ${companyName} and contribute to your technical roadmap.

Maîtrisant le français et l'anglais, je suis particulièrement à l'aise dans les contextes professionnels bilingues. Je suis capable d'analyser la documentation technique en anglais tout en menant les discussions d'équipe et la planification des sprints en français.

Je vous remercie pour le temps consacré à l'examen de ma candidature et serais ravi de vous rencontrer pour un entretien.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

Candidate`;

  // Update State
  STATE.currentTemplate = "custom";
  DOM.currentTemplateDisplay.textContent = `Active Profile: Custom Ingestion`;
  
  STATE.analysis = {
    score: overallScore,
    techScore,
    langScore,
    expScore,
    verdict: overallScore >= 80 ? "Good Match" : "Significant Skill Gaps Found",
    techSkills,
    langSkills,
    gaps: gaps.length > 0 ? gaps : [{ title: "No Major Gaps", action: "Keep refining your technical presentation." }],
    academy: [
      { title: "Bilingual Tech Professional Certification", desc: "A program focused on technical communication in dual-language organizations.", provider: "ApplyWise Academy" }
    ],
    bullets,
    pitches: {
      bilingual: `Hi, I'm a technology professional with experience in software development. Je m'exprime couramment en français et en anglais, ce qui me permet d'évoluer avec aisance au sein d'équipes bilingues. I'm eager to join your team and contribute to your tech stack.`,
      en: `Hi, I'm a software professional. I have hands-on experience building web services and deploying cloud solutions. I'm excited about this opportunity and am looking forward to collaborating in a bilingual setting.`,
      fr: `Bonjour, je suis un professionnel de la technologie. J'ai conçu des architectures fiables et collaboré à des projets d'envergure. Je souhaite rejoindre vos équipes pour collaborer en français et en anglais.`
    },
    coverLetters: {
      hybrid: hybridCoverLetter,
      en: hybridCoverLetter, // Fallback
      fr: hybridCoverLetter // Fallback
    },
    interview: [
      { q: `Can you introduce yourself and describe your technical experience?`, lang: "en" },
      { q: `Pouvez-vous expliquer en français comment vous gérez les priorités techniques lors d'un sprint ?`, lang: "fr" },
      { q: `Why do you want to work in a bilingual tech environment?`, lang: "en" }
    ],
    checklist: [
      "Review custom job description requirements",
      "Draft bilingual cover letter with specific company achievements",
      "Verify French translation of technical projects on resume"
    ]
  };

  STATE.checklist = [...STATE.analysis.checklist];
  updateAllPanels();
}

// --- LIVE GEMINI AI ANALYSIS INTEGRATION ---
async function runLiveGeminiAnalysis(jd, resume) {
  const prompt = `
You are an expert bilingual technical recruiter and career coach in Canada.
Analyze the following Job Description (JD) and Candidate Resume/Profile.
Provide a comprehensive analysis structured exactly in JSON format.

JOB DESCRIPTION:
${jd}

CANDIDATE RESUME:
${resume}

Return ONLY a JSON object with the following keys. Do not include markdown code block formatting (like \`\`\`json) - just raw JSON:
{
  "score": (integer overall match score 0-100),
  "techScore": (integer technical match score 0-100),
  "langScore": (integer language competency score 0-100),
  "expScore": (integer experience score 0-100),
  "verdict": (string 3-6 word overall match verdict),
  "techSkills": [
    { "name": "Skill Name", "match": true/false, "note": "Brief explanation of match or missing experience" }
  ],
  "langSkills": [
    { "name": "Language Requirement", "match": true/false, "note": "Brief explanation" }
  ],
  "gaps": [
    { "title": "Gap Area", "action": "Specific action to bridge this gap" }
  ],
  "academy": [
    { "title": "Course/Cert Name", "desc": "Short description of what they will learn", "provider": "Provider Name" }
  ],
  "bullets": {
    "en": [
      { "original": "Original bullet from resume", "tailored": "Tailored bullet in English incorporating JD keywords" }
    ],
    "fr": [
      { "original": "Original bullet from resume", "tailored": "Tailored bullet in French incorporating JD keywords and correct tech terms" }
    ]
  },
  "pitches": {
    "bilingual": "A 30-second elevator pitch that transitions smoothly between English and French",
    "en": "A 30-second elevator pitch in English",
    "fr": "A 30-second elevator pitch in French"
  },
  "coverLetters": {
    "hybrid": "A Canadian-style cover letter written in a bilingual hybrid format (starts in French, body details in English, concludes in French, proving dual-language capability)",
    "en": "A Canadian-style cover letter written entirely in English",
    "fr": "A Canadian-style cover letter written entirely in French"
  },
  "interview": [
    { "q": "Interview question 1 related to JD requirements (mix of English and French)", "lang": "en/fr/bilingual" },
    { "q": "Interview question 2", "lang": "en/fr/bilingual" },
    { "q": "Interview question 3", "lang": "en/fr/bilingual" },
    { "q": "Interview question 4", "lang": "en/fr/bilingual" },
    { "q": "Interview question 5", "lang": "en/fr/bilingual" }
  ],
  "checklist": [
    "Specific application task 1",
    "Specific application task 2",
    "Specific application task 3"
  ]
}
`;

  const url = `https://generativelanguage.googleapis.com/v1beta/models/${STATE.geminiModel}:generateContent?key=${STATE.geminiApiKey}`;

  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: { responseMimeType: "application/json" }
    })
  });

  if (!response.ok) {
    throw new Error(`Gemini API returned status ${response.status}: ${await response.text()}`);
  }

  const result = await response.json();
  const rawText = result.candidates[0].content.parts[0].text;
  
  // Parse JSON
  const parsed = JSON.parse(rawText);
  
  STATE.currentTemplate = "custom";
  DOM.currentTemplateDisplay.textContent = `Active Profile: Custom Ingestion`;
  
  STATE.analysis = parsed;
  STATE.checklist = [...parsed.checklist];
  
  updateAllPanels();
}

async function getLiveInterviewFeedback(question, answer) {
  const prompt = `
You are a bilingual tech interviewer.
Question asked: "${question}"
Candidate Answer: "${answer}"

Provide a brief, constructive feedback analysis. Discuss:
1. Tech Accuracy (Did they answer the core technical question?)
2. Language/Bilingual Fluency (Is the language professional? Are terms translated correctly?)
3. Specific tips to improve.

Keep the feedback concise, professional, and format in HTML (using paragraphs and lists).
`;

  try {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/${STATE.geminiModel}:generateContent?key=${STATE.geminiApiKey}`;
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }]
      })
    });
    
    if (response.ok) {
      const data = await response.json();
      return data.candidates[0].content.parts[0].text;
    }
  } catch (err) {
    console.error("Error getting live feedback:", err);
  }
  
  return generateSimulatedFeedback(answer);
}

// --- LANGUAGE MODE TOP BAR SELECTION ---
function applyLanguageMode() {
  // Filters panels based on selected language focus
  // Simply adjusts instructions or updates sub-sections
  showToast(`Language focus updated to: ${STATE.activeLang.toUpperCase()}`);
}

// --- UTILITY TOAST ---
function showToast(message) {
  const toast = document.createElement("div");
  toast.style.position = "fixed";
  toast.style.bottom = "24px";
  toast.style.right = "24px";
  toast.style.backgroundColor = "var(--bg-secondary)";
  toast.style.border = "1px solid var(--primary-color)";
  toast.style.color = "var(--text-primary)";
  toast.style.padding = "12px 20px";
  toast.style.borderRadius = "8px";
  toast.style.boxShadow = "var(--shadow-lg)";
  toast.style.zIndex = "1000";
  toast.style.fontSize = "0.85rem";
  toast.style.fontWeight = "600";
  toast.style.animation = "fadeIn 0.3s ease-out";
  toast.textContent = message;
  
  document.body.appendChild(toast);
  
  setTimeout(() => {
    toast.style.animation = "fadeOut 0.3s ease-in";
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// Initialize on load
document.addEventListener("DOMContentLoaded", init);
