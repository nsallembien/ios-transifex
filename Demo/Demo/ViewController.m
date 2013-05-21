//
//  ViewController.m
//  Demo
//
//  Created by Nico Sallembien on 5/21/13.
//  Copyright (c) 2013 Transifex. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

@synthesize userLocale = _userLocale;

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

- (IBAction)changeLocale:(id)sender {

    self.userLocale = [[[NSLocale preferredLanguages] objectAtIndex:0] substringToIndex:2];
    NSString *localeText = [[NSString alloc] initWithFormat:@"Current Locale: %@", self.userLocale];
    self.localeLabel.text = localeText;
}
@end
