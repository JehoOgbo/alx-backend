const Queue = require('bull');

const jobData = {
  phoneNumber: "4282039323",
  message: "This is the message being sent",
};

const notificationQueue = new Queue('push_notification_code');

const job = notificationQueue.add(jobData).then((job) => {
  console.log('Notification job created:', job.id);
}).catch((err) => {
  console.error('Error creating job:', error);
})

notificationQueue.on('completed', (job) => {
  console.log('Notification job completed');
});

notificationQueue.on('failed', (job) => {
  console.log('Notification job failed');
});


// Heres How to do it in Kue Although this is deprecated

// import kue from 'kue';

// // 1. Create the queue
// const queue = kue.createQueue();

// // 2. Define the job data object
// const jobData = {
//   phoneNumber: '4153518780',
//   message: 'This is the code to verify your account'
// };

// // 3. Create a job in the 'push_notification_code' queue
// const job = queue.create('push_notification_code', jobData).save((err) => {
  // Log when the job is created without error
//   if (!err) {
//     console.log(`Notification job created: ${job.id}`);
//   }
// });

// // 4. Handle job completion
// job.on('complete', () => {
//   console.log('Notification job completed');
// });

// // 5. Handle job failure
// job.on('failed', (errorMessage) => {
//   console.log('Notification job failed');
// });
