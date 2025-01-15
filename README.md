![Eduke Logo](https://github.com/theRealSain/eduke/blob/main/images/logo_text_long_bg.png)

# Eduke - Engage, Educate, Evolve

Eduke is an AI-powered academic management system designed to streamline essential educational processes, foster communication between stakeholders, and provide actionable insights into student performance. By leveraging modern technologies, Eduke aims to enhance the learning experience for students, empower teachers, and assist parents in monitoring academic progress.

---

## Features

### 1. User Roles
- **Admin**: Manages the entire system, including user accounts, classes, and subjects.
- **Teacher**: Records attendance, evaluates student performance, and communicates with students and parents.
- **Parent**: Monitors student progress and provides inputs for performance evaluation.
- **Student**: Accesses grades, attendance, and personalized feedback.

### 2. Core Functionalities
- **Attendance Management**: Track daily attendance for each subject.
- **Marks Management**: Record and view student grades and performance.
- **Student Evaluation**: Evaluate students based on various academic factors.
- **AI Chatbot**: Personalized academic assistance and tips for students, parents, and teachers.
- **Chat Feature**: Secure messaging between teachers, parents, and students.
- **Performance Prediction**: Insights into potential academic outcomes using machine learning.

### 3. Database Tables
- **Users**: Manages user credentials and roles.
- **Students**: Contains student-specific details, including roll number and class.
- **Parents**: Stores parent details linked to students.
- **Teachers**: Holds teacher details, including assigned classes.
- **Classes**: Defines class details.
- **Subjects**: Manages subject information.
- **Attendance**: Tracks attendance for each subject.
- **Marks**: Records percentage marks for each student.
- **Student Evaluations**: Academic factor evaluations by teachers and parents.
- **Chat**: Manages communication between users.

---

## Technologies Used

### Backend
- **Python** with **Django Framework**
- **MySQL** for database management

### Frontend
- HTML, CSS, JavaScript
- Bootstrap for responsive UI design

### AI
- **TensorFlow** or **Scikit-learn** for performance prediction
- **OpenAI API** for chatbot functionality

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/theRealSain/eduke.git
   ```

2. Navigate to the project directory:
   ```bash
   cd eduke
   ```

3. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

---

## Contribution Guidelines

1. Fork the repository and create a new branch for your feature or bug fix.
2. Commit your changes with clear and concise messages.
3. Submit a pull request with a detailed description of your changes.


---

## Acknowledgments

- Thanks to the Django and OpenAI communities for providing tools and support.
- Special mention to contributors who make Eduke a success!

---

## Contact

For questions, feedback, or contributions, feel free to reach out:
- **Email**: sainsaburajpnc@gmail.com
- **GitHub**: [theRealSain](https://github.com/theRealSain)
