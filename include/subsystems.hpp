#pragma once

#include "EZ-Template/api.hpp" // IWYU pragma: keep
#include "api.h" // IWYU pragma: keep

extern Drive chassis;

// Your motors, sensors, etc. should go here.  Below are examples
// Clamp Code
inline pros::adi::DigitalOut Clamp(5, false);
// Clamp Code
inline pros::adi::DigitalOut Doinker(1, false);
// Intake Code
//pros::Motor Intake (19, pros::E_MOTOR_GEARSET_06, false, pros::E_MOTOR_ENCODER_DEGREES);
inline pros::Motor IntakeA(-20);
inline pros::Motor IntakeSmall(-13);
// LB Code
// 5.5 W Config
inline pros::Motor LadyBrown(2);
/*
pros::Motor LB1 (7, pros::E_MOTOR_GEARSET_18, false, pros::E_MOTOR_ENCODER_DEGREES);
pros::Motor LB2 (13, pros::E_MOTOR_GEARSET_18, true, pros::E_MOTOR_ENCODER_DEGREES);*/
// Motor Group Declaration
inline pros::v5::MotorGroup Intake({-13, -20});
