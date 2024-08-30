const user = {
    name: "Piyush Sharma",
    designation: "Senior Software Engineer",
    company: "Infuse Consulting",
    hobbies: ["Reading", "Listening to music", "Collecting stamps"]
}



const printUserProfile = () => {
    // Piyush Sharma is a Senior Software Engineer at Infuse Consulting. He likes Reading, Listening to music and Collecting stamps
    const { name, designation, company, hobbies } = user;
    const formattedHobbies = hobbies.map((hobby, index) => {
        if (index === hobbies.length - 1) {
            return `and ${hobby}`;
        } else {
            return hobby;
        }
    }).join(', ');
    console.log(`${name} is a ${designation} at ${company}. He likes ${formattedHobbies}.`);
}

printUserProfile()

