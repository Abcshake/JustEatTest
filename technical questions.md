1. How long did you spend on the technical test? What would you add to your solution if you had more time? If you didn't spend much time on the technical test then use this as an opportunity to explain what you would add.

Answer: I spend 1 hour writing the test and one and half hour to debug it. If I could spend more time on the test then I would make another file in order to create page objects for the web elements that are used in the test. So that way the page objects can be easily used for other tests. I would also try to validate the number of restaurants the search query yeilded and make sure the number is greater than 0 using regular expressions. In a complete project project a batch file would be created so tests can run on any local machine without setting up Visual studio or downloading Chromedriver

2. What do you think is the most interesting trend in test automation?

Answer: One of the most interesting development in test automation is the rise of keyword driven frameworks. Where keywords are written in a business readable language so that the test scenarios can be understood without programming expertise. Robot Framwork is popular framework that uses easily understandable keywords as well as Cucumber. Another more recent development is the user of Azure DevOps to implement automated load and performance testing. Azure Devops uses the Azure cloud service to generate a load from different regions in order to the test the responsiveness and stability of an application.

3. How would you implement test automation in a legacy application? Have you ever had to do this?

Answer: When testing legacy application the standard QA procedure is to create a regression suite. The regression suite contains the test cases that evaluates all the business logic of the application. If the old application is going to be integrated into a new system multiple regression cycles can be required. The best way to run these cycles is to prepare automation test cases for these cycles. I have helped prepare automation regression suites while working with CIBC digital

4. How would you improve the customer experience of the JUST EAT website?

Answer: One way to improve the customer experience on the Just Eat website is to give users different options for finding near by restaurants. There could a service to auto defect the customers location in real time and query the data base for the closest restuarant. The site can make also postal code suggestions if the customer mispells or forgets parts of their postal code

5. Please describe yourself using JSON.

Answer: Example email in JSON format

{

    headers: [  # in an array since order matters
        { name: 'Subject', value: 'An email' },
        { name: 'Date',    value: 'Thu, 10 Dec 2019 21:00:32 -0800' },
        { name: 'From',    value: 'avi@abc.com' },
        { name: 'To',      value: 'paul@goo.com' }
        { name: 'Sender',  value: 'paul@goo.com' }
        { name: 'Reply-to', value: 'paul@goo.com' }
    ],
    from: 'From blah blah...',
    body: {
                id: 'partid-1',
                type: 'text/plain',
                sections: [
                    {
                        type: 'greeting',
                        text: 'Dear Paul,'
                    },
                    {
                        type: 'normal',
                        text: 'How's it going',
                    },
                    {
                        type: 'Signature',
                        text: 'Yours, Avi'
                    },
                    
           }
  }
