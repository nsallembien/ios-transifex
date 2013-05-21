//
//  ViewController.m
//  Demo
//
//  Created by Nico Sallembien on 5/20/13.
//  Copyright (c) 2013 Transifex. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

@synthesize userName = _userName;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)changeGreeting:(id)sender {

    self.userName = self.textField.text;
    
    NSString *nameString = self.userName;
    if ([nameString length] == 0) {
        nameString = NSLocalizedString(@"WORLD", @"The default name in the format");
    }
    NSString *greeting = [[NSString alloc] initWithFormat:NSLocalizedString(@"HELLO", @"The greeting format displayed"), nameString];
    self.label.text = greeting;

}

- (BOOL)textFieldShouldReturn:(UITextField *)theTextField {
    if (theTextField == self.textField) {
        [theTextField resignFirstResponder];
    }
    return YES;
}

@end
