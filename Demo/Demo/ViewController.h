//
//  ViewController.h
//  Demo
//
//  Created by Nico Sallembien on 5/20/13.
//  Copyright (c) 2013 Transifex. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController <UITextFieldDelegate>

@property (weak, nonatomic) IBOutlet UITextField *textField;
@property (weak, nonatomic) IBOutlet UILabel *label;

@property (copy, nonatomic) NSString *userName;

- (IBAction)changeGreeting:(id)sender;

@end
